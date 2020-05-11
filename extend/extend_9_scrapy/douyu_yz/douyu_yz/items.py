# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuYzItem(scrapy.Item):
    icon = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    hot = scrapy.Field()
