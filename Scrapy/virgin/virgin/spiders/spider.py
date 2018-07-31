# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from virgin.items import virginItem

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'virgin'
    start_urls = [
        'https://www.virginmobile.cl/tarifas/planes-cuenta-controlada',
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="box-planes clearfix"]'):
            ml_item = virginItem()
            ml_item['Plan'] = quote.xpath('normalize-space(.//p[@class="nombrePlan"]/text())').extract()
            ml_item['Gigas'] = quote.xpath('normalize-space(.//div/span[@class="numeroGiga"]/text())').extract()
            ml_item['Monto'] = quote.xpath('normalize-space(.//div/span[@class="precioPlan"]/text())').extract()
            ml_item['Promocion'] = quote.xpath('normalize-space(.//div/p[@class="vigencia text-right"]/text())').extract()
            ml_item['Detalle1'] = quote.xpath('normalize-space(.//div/p[@class="min-300"]/text())').extract()
            ml_item['Detalle0'] = quote.xpath('normalize-space(.//div/span[@class="numeroMin"]/text())').extract()

            yield ml_item
                
                

        


