# -*- coding: utf-8 -*-
import scrapy
from day29.items import MovieItem
import requests

class MoviespiderSpider(scrapy.Spider):
    name = 'MovieSpider'
    allowed_domains = ['dytt8.net', 'ygdy8.net']
    start_urls = ['http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html']
    offset = 1

    def parse(self, response):
        urls = response.css(".ulink::attr(href)").extract()
        print("获取结果： ", urls)
        for url in urls:
            url = "http://www.ygdy8.net" + url
            print("url: ", url)
            yield scrapy.Request(url, callback=self.parse_item)

        if self.offset < 10:
            self.offset += 1
            new_page_url = "http://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html".format(self.offset)
            yield scrapy.Request(new_page_url, callback=self.parse)

    def parse_item(self, response):
        print("response:\r\n", response)
        name = response.css("#header > div > div.bd2 > div.bd3 > div.bd3r > div.co_area2 > div.title_all > h1 > font::text").extract()[0]
        icon = response.css("#Zoom img::attr('src')").extract()[0]
        url = response.css("#Zoom td > a::attr('href')").extract()[0]

        item = MovieItem()
        item["name"] = name
        item["icon"] = icon
        item["url"] = url

        return item