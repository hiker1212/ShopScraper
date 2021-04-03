import scrapy

class ShopSpider(scrapy.Spider):
    name = "mediamarkt"
    allowed_domains = ['mediamarkt.es']
    start_urls = [
        'https://www.mediamarkt.es/es/category/_frigor%C3%ADficos-combinados-702140.html',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        self.logger.info(' - URL: %s', response.url)
        self.logger.info(' - xpath: %s', response.xpath)
        for h3 in response.xpath('//h3').getall():
            yield {"title": h3}