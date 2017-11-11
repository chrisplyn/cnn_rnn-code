import scrapy

class lyricsItem(scrapy.Item):
    # define the fields for your item here like:
    content = scrapy.Field()

class lyricsSpider(scrapy.Spider):
	name = "lyrics"
	start_urls = ["http://www.allthelyrics.com/lyrics/taylor_swift"]

	BASE_URL = 'http://www.allthelyrics.com'

	def parse(self, response):
		links = response.xpath('//div[@class="nodetype-artist-content-lyrics-all"]//@href').extract()
		for link in links:
			absolute_url = self.BASE_URL + link
			yield scrapy.Request(absolute_url, callback=self.parse_attr)

	def parse_attr(self, response):
		item = lyricsItem()
		item["content"] = response.xpath('//div[@class="content-text-inner"]//text()').extract()
		return item