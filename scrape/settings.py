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
FORM_DATA = None

# Edit Config Here
DEPTH_LIMIT = 0  # 0 = no limit

#app1_admin
# START_URL = "https://app1.com/admin/index.php?page=login"
# FORM_DATA = {'adminname': 'admin', 'password': 'admin'}

#app1 user
# START_URL = "https://app1.com/users/login.php"
# FORM_DATA = {'username': 'bryce', 'password': 'bryce'}
# CONTENT_TYPE = "application/x-www-form-urlencoded"

#app3 nologin
START_URL = "https://app3.com"

#app5 nologin
# START_URL = "https://app5.com"

#app6
# START_URL = "https://app6.com/zimplit.php"
# FORM_DATA = {'username': 'admin', 'password': 'admin'}

#app7 admin
# START_URL = "https://app7.com/oc-admin/index.php?page=login"
# FORM_DATA = {'user': 'admin', 'password': 'admin'}

#app8 admin
# START_URL = "https://app8.com/upload/admin/"
# FORM_DATA = {'username': 'admin', 'password': 'admin'}

#app9 admin
# START_URL = "https://app9.com/index-test.php/site/login"
# FORM_DATA = {"LoginForm[username]": "admin", "LoginForm[password]": "admin"}

#app9 user
# START_URL = "https://app9.com/index-test.php/site/login"
# FORM_DATA = {"LoginForm[username]": "test", "LoginForm[password]": "test"}

#app11 user
START_URL = "https://app11.com/ajax_login.php"
FORM_DATA = {'username': 'admin', 'password': 'admin'}