# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy import signals, log


# class JsonWriterPipeline(object):
#     def __init__(self):
#         self.file = open('data/items.json', 'wb')
#         log.msg("JsonWriterPipeline instance created.", log.INFO)
#
#     def process_item(self, item, spider):
#         print item
#         line = json.dumps(dict(item)) + "\n"
#         self.file.write(line)
#         log.msg("JsonWriterPipeline process_item()", log.INFO)
