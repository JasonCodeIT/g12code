__author__ = 'Jason Poh'
import re
from scrapy.utils.project import get_project_settings
from scrapy.spider import Spider
from scrapy.http import Request, HtmlResponse
from scrape.items import FormItem
from urlparse import urlparse
from scrapy import signals, log


class ScannerSpider(Spider):
    name = "scanner"

    def __init__(self, **kw):
        super(ScannerSpider, self).__init__(**kw)
        url = kw.get('url')
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://%s/' % url
        self.url = url
        self.allowed_domains = [re.sub(r'^www\.', '', urlparse(url).hostname)]

    def start_requests(self):
        return [Request(self.url, callback=self.parse, dont_filter=True)]

    def parse(self, response):
        for sel in response.xpath('//form'):
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
        # Saving the form item
        return form
