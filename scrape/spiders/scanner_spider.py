__author__ = 'Jason Poh'
import re
import urllib

# from scrape.settings import FORM_DATA, CONTENT_TYPE
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.http import Request, FormRequest
from scrape.items import FormItem
from urlparse import urlparse
from scrapy import log
from scrapy import Selector


class ScannerSpider(CrawlSpider):
    seed = 999
    name = "scanner"
    FORM_DATA = None
    CONTENT_TYPE = None
    # matching app1.com/calendar.php?date= causing infinite follow
    # matching logout pages so scrapy will not logout from a session
    re1 = '=[1-2][0-9]{9}|logout|page=[0-9]{2}|upgrader|updater|delete|remove'

    rules = (
        Rule(LxmlLinkExtractor(unique=True, deny=re1), callback='parse_item', follow=False),
    )
    allowed_domains = None
    start_urls = []
    handle_httpstatus_list = [500, 301, 302]

    def __init__(self, **kw):
        super(ScannerSpider, self).__init__(**kw)
        url = kw.get('url')
        self.FORM_DATA = kw.get('formdata')
        self.CONTENT_TYPE = kw.get('contenttype')
        self.seed = kw.get('seed')
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://%s/' % url
        self.start_urls = [url]
        self.allowed_domains = [re.sub(r'^www\.', '', urlparse(url).hostname)]

    # Entry point of spider
    def parse_start_url(self, response):
        if self.FORM_DATA is not None and str(len(self.FORM_DATA)) > 0:
            self.log("Starting crawling WITH login credentials...")
            if self.CONTENT_TYPE is None or len(self.CONTENT_TYPE) < 1:
                return [FormRequest.from_response(response,
                                                  formdata=self.FORM_DATA,
                                                  callback=self.parse_item,
                                                 )]

            return Request(self.start_urls[0],
                      self.parse_item,
                      method="POST",
                      body=urllib.urlencode(self.FORM_DATA),
                      headers={'Content-Type': self.CONTENT_TYPE})
        else:
            self.log("Starting crawling WITHOUT login credentials...")
            return self.parse_item(response)

    # Subsequent crawling in spider
    def parse_item(self, response):
        # Extracts all Cookies
        cookie_item = self._process_cookie(response)
        yield cookie_item

        # Extracts all headers
        # headers = self._process_headers(response)
        # yield headers

        # Extracts all query strings
        if "?" in response.url:
            regex = "\\?([a-zA-Z0-9_]+=[/a-zA-Z0-9_\\-\\.]+)(&[a-zA-Z0-9_]+=[/a-zA-Z0-9_\\-\\.]+)*"
            rg = re.compile(regex, re.IGNORECASE|re.DOTALL)
            mm = rg.findall(response.url)
            mydict = {}
            isAction = 0
            for m in mm:
                querystring = "".join(m)
                qs_url = response.url.replace("?"+querystring, "", 1)
                querystring_list = querystring.split("&")
                form = FormItem()
                form['url'] = qs_url
                form['method'] = 'GET'
                for qs in querystring_list:
                    tmp_qs = qs.split("=")
                    if len(tmp_qs) == 2:
                        qs_key = tmp_qs[0]
                        if qs_key == 'action':
                            isAction += 1
                        qs_val = tmp_qs[1]
                        mydict[qs_key] = qs_val
                form['form_items'] = mydict
                form['seed'] = self.seed
                yield form

                #patch for action=
                if isAction == 1:
                    mydict = {}
                    form = FormItem()
                    form['url'] = qs_url
                    form['method'] = 'GET'
                    mydict['action'] = 'load1'
                    mydict['file'] = 'index.html'
                    form['form_items'] = mydict
                    form['seed'] = self.seed
                    yield form
                    mydict = {}
                    form = FormItem()
                    form['url'] = qs_url
                    form['method'] = 'GET'
                    mydict['action'] = 'loadExternalHtml'
                    mydict['file'] = 'index.html'
                    form['form_items'] = mydict
                    form['seed'] = self.seed
                    yield form

        # Process all inline script tags
        match_url_re = "['|\"]([a-zA-Z0-9_-]+[/a-zA-Z0-9_\\-\\.]*[?][/a-zA-Z0-9_\\-&=]*)['|\"]"
        rg = re.compile(match_url_re, re.IGNORECASE | re.DOTALL)
        mm = rg.findall(response.body)
        for m in mm:
            ajax_url = "".join(m)
            script_url = self.__to_absolute_url(response.url, ajax_url)
            if "file" in script_url or "dir" in script_url:
                form_item = FormItem()
                form_item['url'] = script_url
                form_item['method'] = 'POST'
                mydict = {}
                mydict['directory'] = ''
                mydict['dir'] = ''
                mydict['file'] =  ''
                form_item['form_items'] = mydict
                form_item['seed'] = self.seed
                yield form_item
            if self._filter_requests(script_url):
                yield Request(script_url, callback=self.parse_item)


        # Process all external script tags
        for sel in response.xpath('//script'):
            url_list = sel.xpath('@src').extract()
            if len(url_list) > 0:
                script_url = self.__to_absolute_url(response.url, url_list[0])
                if self._filter_requests(script_url):
                    yield Request(script_url, callback=self.parse_item)

        for sel in response.xpath('//iframe'):
            url_list = sel.xpath('@src').extract()
            if len(url_list) > 0:
                script_url = self.__to_absolute_url(response.url, url_list[0])
                if self._filter_requests(script_url):
                    yield Request(script_url, callback=self.parse_item)

        # Process all anchor tags
        match_url_re = "<a href=[\"|']([a-zA-Z:/\\.0-9?=&;-]+)"
        rg = re.compile(match_url_re, re.IGNORECASE | re.DOTALL)
        mm = rg.findall(response.body)
        for m in mm:
            ajax_url = "".join(m)
            script_url = self.__to_absolute_url(response.url, ajax_url)
            if self._filter_requests(script_url):
                    yield Request(script_url, callback=self.parse_item)


        # Extracts url from possible ajax query in javascript file
        for body_line in response.body.lower().split(";"):
            if "open" not in body_line or "get" not in body_line:
                continue
            # Matches blah/moreblah/a/b.php?queryString=
            rg = re.compile("([a-zA-Z0-9_]+)(/[a-zA-Z0-9_]+)+(\\.[a-zA-Z]+\\?[a-zA-Z0-9_]+)", re.IGNORECASE | re.DOTALL)
            mm = rg.findall(body_line)
            for m in mm:
                ajax_url = "".join(m)
                url_parts = ajax_url.split("?")
                form = FormItem()
                form['url'] = self.__to_absolute_url(response.url, url_parts[0])
                form['method'] = 'GET'
                form['form_items'] = [url_parts[1]]
                form['seed'] = self.seed
                yield form

        # Process all form tags
        for form in response.xpath('//form').extract():
            sel = Selector(text=form, type='html')
            form_input = self._process_form(sel, response)
            yield form_input

    def __to_absolute_url(self, base_url, link):
        '''
        Convert relative URL to absolute URL
        '''
        import urlparse
        link = urlparse.urljoin(base_url, link)
        return link

    def _process_headers(self, response):
        form = FormItem()
        form['url'] = response.url
        form['method'] = "Header"
        form['form_items'] = response.headers.keys()
        return form

    def _process_form(self, sel, response):
        form = FormItem()
        form['url'] = response.url

        # Extracts form action URL
        action_url = sel.xpath('//@action').extract()
        if len(action_url) != 0:
            form['target_url'] = self.__to_absolute_url(response.url, action_url[0])
        else:
            form['target_url'] = response.url

        # Extracts the method used in form (i.e. GET or POST)
        form['method'] = sel.xpath('//@method').extract()
        if len(form['method']) == 0:
            form['method'] = "GET"
        else:
            form['method'] = form['method'][0]

        # Extracts all params from all inputs in form
        params = sel.xpath('//*/@name').extract()
        self.log('[DEBUG-FORM]: ' + "".join(params))
        mydict = {}
        for p in params:
            mydict[p] = ''
        form['form_items'] = mydict
        # return form

        # Extracts all params from all file inputs in form
        params = sel.xpath('//input[@type=\'file\']/@name').extract()
        if len(params) > 0:
            mydict = {}
            for p in params:
                mydict[p] = ''
            form['file_items'] = mydict
        form['seed'] = self.seed
        return form

    def _process_cookie(self, response):
        if "Cookie" not in response.request.headers:
            return None
        cookie = response.request.headers['Cookie']
        cookie_item = FormItem()
        cookie_item['url'] = response.request.url
        cookie_item['method'] = 'COOKIE'
        mydict = {}
        cookies = cookie.split(";")
        for c in cookies:
            cc = c.split("=", 1)
            mydict[cc[0].strip()] = cc[1].strip()
        cookie_item['form_items'] = mydict
        cookie_item['seed'] = self.seed
        return cookie_item

    def _filter_requests(self, url):
        pass_test = True
        rg = re.compile(self.re1, re.IGNORECASE|re.DOTALL)
        mm = rg.findall(url)
        for m in mm:
            querystring = "".join(m)
            pass_test = False
        return pass_test