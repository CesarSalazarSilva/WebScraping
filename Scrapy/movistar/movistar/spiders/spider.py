# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from movistar.items import movistarItem

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'movistar'
    start_urls = [
        'https://planes.movistar.cl/planes-multimedia-renovacion',
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="item"]'):
            ml_item = movistarItem()
            ml_item['Plan'] = quote.xpath('normalize-space(.//a[@class="titulo"]/text())').extract()
            ml_item['plan'] = quote.xpath('normalize-space(.//div[@class="titulo"]/text())').extract()
            ml_item['Gigas'] = quote.xpath('normalize-space(.//h2[@class="titulo"]/text())').extract()
            ml_item['Monto'] = quote.xpath('normalize-space(.//span[@class="monto"]/text())').extract()
            ml_item['Promocion'] = quote.xpath('normalize-space(.//div[@class="cucardaCyber"]/text())').extract()
            ml_item['Detalle1'] = quote.xpath('normalize-space(.//span[@class="voz"]/text())').extract()
            #ml_item['Detalle0'] = quote.xpath('normalize-space(.//div/span[@class="numeroMin"]/text())').extract()
            yield ml_item
                
                

        


