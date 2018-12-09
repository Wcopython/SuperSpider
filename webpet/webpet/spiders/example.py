# -*- coding: utf-8 -*-
import scrapy

from webpet.items import WebpetItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ["meijutt.com"]
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for each_movie in movies:
            item = WebpetItem()
            item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
            item['belongto'] = each_movie.xpath('./span[@class="mjjq"]/text()').extract()[0]
            list = each_movie.xpath('./div[contains(@class,"lasted-time")]/font/text()').extract()
            if len(list)>0:
                item['updatetime']=list[0]
            else:
                item['updatetime']='无'
            yield item
