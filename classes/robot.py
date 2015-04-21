from operator import concat

__author__ = 'Jason Poh'


import os
import json

# spider
from scrape.spiders.scanner_spider import ScannerSpider

# scrapy api
from scrapy import signals, log
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings


class Robot(object):

    starturl = None
    formdata = {}
    contenttype = None
    seed_idx = -1

    def __init__(self, seeds):
        self.crawlers_running = 0
        self.seeds = seeds
        return

    def transform(self, scrapy_out_file, endpoint_file):
        entries = open(scrapy_out_file, 'r').readlines()
        endpoints = []

        for entry in entries:
            entry = json.loads(entry)
            endpoints.append({
                'seed': entry['seed'],
                'url': entry['url'],
                'target': entry['target_url'] if 'target_url' in entry else entry['url'],
                'method': entry['method'][0],
                'params': entry['form_items'],
                'files': entry['file_items'] if 'file_items' in entry else None
            })

        json.dump(endpoints, open(endpoint_file, 'w'), indent=True)

    def spider_closing(self):
        self.crawlers_running -= 1
        if self.crawlers_running == 0 :
            reactor.stop()

    def crawl(self):
        '''
            Crawls using scrapy module

            # TODO: Crawl the links in the given start_url on the same domain

            :return:None
        '''

        # delete existing file, if any
        if os.path.isfile("data/items.json"):
            os.remove("data/items.json")

        # read seed file
        with open(self.seeds) as data_file:
            data = json.load(data_file)

        for seed in data:
            self.seed_idx += 1 # Counter
            self.starturl = None
            self.formdata = None
            self.contenttype = None

            if seed['auth'] is not None:
                self.formdata = seed['auth']['params']
                self.starturl = seed['auth']['url']
                self.contenttype = seed['auth']['content_type']
            else:
                self.starturl = seed['start_url']



            # Start Crawling All Below

            spider = ScannerSpider(url=self.starturl, formdata=self.formdata, contenttype=self.contenttype, seed=self.seed_idx)
            crawler = Crawler(Settings())
            crawler.settings.setdict({
                'START_URL': self.starturl,
                'FORM_DATA': self.formdata,
                'FEED_URI': "data/items.json",
                'AJAXCRAWL_ENABLED': True,
                'COOKIES_DEBUG': True,
                'USER_AGAENT': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.60 Safari/537.36"
                })
            crawler.signals.connect(self.spider_closing, signal=signals.spider_closed)
            crawler.configure()
            crawler.crawl(spider)
            self.crawlers_running += 1
            crawler.start()
        return None