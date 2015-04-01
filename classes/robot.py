__author__ = 'Jason Poh'
import os
import json
from classes import phase1
from helpers import jsonhelper, filehelper

# spider
from scrape.spiders.scanner_spider import ScannerSpider

# scrapy api
from scrapy import signals, log
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings


class Robot(object):

    def __init__(self, start_url, depth=10, max_urls=10):
        '''
            :param start_url: the start URL to crawl from
            :param depth: the depth to crawl (optional)
            :param max_urls: maximum number of distinct URLs to crawl (optional)
            :return:
        '''
        self.start_url = start_url
        self.depth = depth          # int, optional
        self.max_urls = max_urls    # int, optional

    def spider_closing(spider):
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

        spider = ScannerSpider(url=self.start_url)
        crawler = Crawler(Settings())
        crawler.settings.setdict({
            'FEED_URI': "data/items.json",
            'AJAXCRAWL_ENABLED': True,
            'COOKIES_DEBUG': True,
            'USER_AGAENT': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.60 Safari/537.36"
            })
        crawler.signals.connect(self.spider_closing, signal=signals.spider_closed)
        crawler.configure()
        crawler.crawl(spider)
        crawler.start()
        log.start(loglevel=log.DEBUG)
        reactor.run()
        return None