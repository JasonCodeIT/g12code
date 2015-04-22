# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class FormItem(scrapy.Item):
    # define the fields for your item here like:
    seed = scrapy.Field()
    url = scrapy.Field()
    target_url = scrapy.Field()
    form_items = scrapy.Field()
    method = scrapy.Field()
    file_items = scrapy.Field()
    pass
