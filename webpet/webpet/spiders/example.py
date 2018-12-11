# -*- coding: utf-8 -*-
import io
import sys
from urllib import request

import scrapy

from webpet.items import WebpetItem
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ["baidu.com"]
    # start_urls = ['https://sou.zhaopin.com/?jl=530&sf=25001&st=35000&kw=%E5%89%8D%E7%AB%AF&kt=3']
    start_urls = ['https://sou.zhaopin.com']

    def parse(self, response):
        print(response.text)
        movies = response.xpath('//div[@class="contentpile__content__wrapper clearfix"]')
        # print(len(movies))
        for each_movie in movies:
            # print(each_movie)
            item = WebpetItem()
            item['name'] = each_movie.xpath('.//a[contains(@class,"company_title")]/@title').extract()[0]
            item['belongto'] = each_movie.xpath('.//p[@class="contentpile__content__wrapper__item__info__box__job__saray"]/text()').extract()[0]
            item['updatetime'] = each_movie.xpath('.//span[@class="contentpile__content__wrapper__item__info__box__jobname__title"]/@title').extract()[0]
            yield item
                # yield scrapy.Request(url="http://www.meijutt.com"+each_movie.xpath('./h5/a/@href').extract()[0], callback=self.parse_detail, meta={'data': item})

        # # 下一页
        # next_url = response.xpath('//a[@id="next"]/@href').extract()[0]
        # next_url = request.urljoin(response.url, next_url)
        #
        # # 是否是最后一页
        # last_page = response.xpath('//a[@id="next"]/@class').extract()
        # last_page = self.getvalue(last_page)
        # if last_page != 'noactive':
        #     yield scrapy.Request(url=next_url, callback=self.parse)

    def parse_detail(self, response):
        # print('~~~~~~~~~~~detail~~~~~~~~~~~~`')
        # print(response.text)
        item = response.meta['data']
        # with open('detail.html', 'w', encoding='utf-8') as f:
        #     f.write(response.body.decode('utf-8'))
        # 工作职责
        originName = response.xpath('//div[@class="o_big_img_bg_b"]/img/@src').extract()[0]
        # print(duty)#字符串列表
        # print(duty)
        # duty = ''.join(duty)
        item['originName'] = originName
        # 工作要求
        # rq = response.xpath('//tr[@class="c"][2]//li/text()').extract()
        # rq = ''.join(rq)
        # item['rq'] = rq
        # print(duty+'\n')
        # print(rq)
        # print('~~~~~~~~~~~~~~~`')
        yield item
