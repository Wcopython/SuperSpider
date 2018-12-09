# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter
from openpyxl import Workbook


class WebpetPipeline(object):
    # def process_item(self, item, spider):
    #     with open("my_meiju.txt", 'a') as fp:
    #         fp.write(item['name']+'\n')

    def open_spider(self, spider):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['最新美剧','小分类','更新时间'])  # 设置表头


    def process_item(self, item, spider):
        line = [item['name'],item['belongto'],item['updatetime']]  # 把数据中每一项整理出来
        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        self.wb.save('tuniu.xlsx')  # 保存xlsx文件
        return item


