# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json

class DouyuYzPipeline:
    def open_spider(self, spider):
        print("启动的时候执行!")
        self.file = open("yanzi.txt", "wb")

    def process_item(self, item, spider):
        json_str = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(json_str.encode())
        return item

    def close_spider(self, spider):
        print("结束的时候执行!")
        self.file.close()
