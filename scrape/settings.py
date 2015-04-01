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

CONTENT_TYPE = None

# Edit Config Here
DEPTH_LIMIT = 0  # 0 = no limit

#app1_admin
# START_URL = "https://app1.com/admin/index.php?page=login"
# FORM_DATA = {'adminname': 'admin', 'password': 'admin'}

#app1 user
# START_URL = "https://app1.com/users/login.php"
# FORM_DATA = {'username': 'bryce', 'password': 'bryce'} #None or Dictionary to
# CONTENT_TYPE = "application/x-www-form-urlencoded"

#app6
START_URL = "https://app6.com/zimplit.php"
FORM_DATA = {'username': 'admin', 'password': 'admin'} #None or Dictionary to login

