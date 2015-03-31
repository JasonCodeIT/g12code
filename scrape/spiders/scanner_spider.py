__author__ = 'Jason Poh'
import re

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.http import Request
from scrape.items import FormItem
from urlparse import urlparse
from scrapy import log


class ScannerSpider(CrawlSpider):
    name = "scanner"

    # matching app1.com/calendar.php?date= causing infinite follow
    re1 = '.*?(calendar\\.php)(\\?)(date)(=)'

    rules = (
        Rule(LxmlLinkExtractor(unique=True, deny=re1), callback='parse_url', follow=True),
    )
    allowed_domains = None
    start_urls = []

    def __init__(self, **kw):
        super(ScannerSpider, self).__init__(**kw)
        url = kw.get('url')
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://%s/' % url
        self.start_urls = [url]
        self.allowed_domains = [re.sub(r'^www\.', '', urlparse(url).hostname)]

    def __to_absolute_url(self, base_url, link):
        '''
        Convert relative URL to absolute URL
        '''

        import urlparse
        link = urlparse.urljoin(base_url, link)
        return link

    def parse_start_url(self, response):
        return self.parse_url(response)

    def _process_headers(self, response):
        form = FormItem()
        form['url'] = [re.sub(r'^www\.', '', urlparse(response.url).hostname)]
        form['method'] = "Header"
        form['form_items'] = response.headers.keys()
        return form

    def _process_form(self, sel):
        form = FormItem()
        # Extracts form action URL
        form['url'] = sel.xpath('@action').extract()
        if len(form['url']) == 0:
            form['url'] = ["/"]

        # Extracts the method used in form (i.e. GET or POST)
        form['method'] = sel.xpath('@method').extract()
        if len(form['method']) == 0:
            form['method'] = ["GET"]

        # Extracts all params from all inputs in form
        params = sel.xpath('//*/@name').extract()
        form['form_items'] = params
        return form

    def parse_url(self, response):
        # Extracts all headers
        headers = self._process_headers(response)
        yield headers

        # Process all script tags
        for sel in response.xpath('//script'):
            script_url = self.__to_absolute_url(response.url, sel.xpath('@src').extract()[0])
            yield Request(script_url, callback=self.parse_url)

        # Extracts url from possible ajax query in javascript file
        for body_line in response.body.lower().split(";"):
            if "open" not in body_line or "get" not in body_line:
                continue
            #matches blah/moreblah/a/b.php?queryString=
            rg = re.compile("([a-zA-Z0-9_]+)(/[a-zA-Z0-9_]+)+(\\.[a-zA-Z]+\\?[a-zA-Z0-9_]+)",re.IGNORECASE|re.DOTALL)
            mm = rg.findall(body_line)
            for m in mm:
                ajax_url = "".join(m)
                url_parts = ajax_url.split("?")
                form = FormItem()
                form['url'] = self.__to_absolute_url(response.url, url_parts[0])
                form['method'] = 'GET'
                form['form_items'] = [url_parts[1]]
                yield form

        # Process all form tags
        for sel in response.xpath('//form'):
            form_input = self._process_form(sel)
            yield form_input

