# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings

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


class YzImagePileline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        image_url = item["icon"]
        print("request image url...")
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_path = [x["path"] for ok, x in results if ok]
        item["image_path"] = self.IMAGES_STORE + "/" + image_path[0]
        print("download image url...")
        return item
