#coding:utf-8
import scrapy
from scrapy.spiders import CrawlSpider
from baidu.items import BaiduItem
from scrapy.http import Request
class baiduSpider(CrawlSpider):
	name = 'baidu'
	allowed_domains = ['baidu.com']
	start_urls = ['http://baike.baidu.com/view/284853.htm']
	
	def __init__(self):
		self.x=0
    
	def parse(self,response):
		url=response.url
		title=response.xpath("//*[@class='lemmaWgt-lemmaTitle-title']/h1/text()").extract()[0]
		new_urls=response.xpath("//*[starts-with(@href,'/item/')]/@href").extract()
		summary=response.xpath("//*[@class='lemma-summary']/div")
		summary=summary.xpath('string(.)').extract()[0]
		item=BaiduItem(url=url,title=title,summary=summary)
		yield item
		for url in new_urls:
			self.x+=1
			if self.x>100:
				break
			self.url=url
			yield Request(response.urljoin(url=url),
			callback=self.parse)
		
		

