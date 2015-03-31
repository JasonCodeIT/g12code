# -*- coding: utf-8 -*-

# Scrapy settings for scrape project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#



BOT_NAME = 'scrape'

SPIDER_MODULES = ['scrape.spiders']
NEWSPIDER_MODULE = 'scrape.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.60 Safari/537.36'

# Edit Config Here
DEPTH_LIMIT = 0  # 0 = no limit

#app6
START_URL = "https://app6.com/zimplit.php"
FORM_DATA = {'username': 'admin', 'password': 'admin'} #None or Dictionary to login

