import scrapy

from scrapy.loader import ItemLoader
from ..items import BrsspaItem
from itemloaders.processors import TakeFirst


class BrsspaSpider(scrapy.Spider):
	name = 'brsspa'
	start_urls = ['https://brsspa.it/archivio-news/']

	def parse(self, response):
		post_links = response.xpath('//div[@class="vc_col-sm-12 vc_gitem-col vc_gitem-col-align-"]')
		for link in post_links:
			post_link = link.xpath('.//a[@class="vc_general vc_btn3 vc_btn3-size-xs vc_btn3-shape-square vc_btn3-style-custom"]/@href').get()
			date = link.xpath('.//div[@style="text-align: left"]/text()').get()
			yield response.follow(post_link, self.parse_post, cb_kwargs=dict(date=date))

	def parse_post(self, response, date):
		title = response.xpath('//h1[contains(@class, "page-title")]/text()').get()
		description = response.xpath('//div[@class="mk-single-content clearfix"]//p[normalize-space()]//text()').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()

		item = ItemLoader(item=BrsspaItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
