# -*- coding: utf-8 -*-
import scrapy
import json
from douyu_yz.items import DouyuYzItem

class YanzhispiderSpider(scrapy.Spider):
    name = 'YanZhiSpider'
    allowed_domains = ['douyu.com']
    start_urls = ['https://m.douyu.com/api/room/list?page=1&type=yz']

    def parse(self, response):
        json_data = json.loads(response.text)

        users = json_data["data"]["list"]

        for user in users:
            item = DouyuYzItem()
            item["name"] = user["nickname"]
            item["icon"] = user["roomSrc"]
            item["title"] = user["roomName"]
            item["hot"] = user["hn"]

            yield item
