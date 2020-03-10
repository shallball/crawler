# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem
class BaiduPipeline(object):
	def __init__(self):
		self.file = open('baidu.txt', 'w')
	def process_item(self, item, spider):			
		self.file.write(str(item)+'/n')
		return item

