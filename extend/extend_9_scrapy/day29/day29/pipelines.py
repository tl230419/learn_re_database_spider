# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from day29.db.models import Session, Movie
from day29.items import MovieItem

class Day29Pipeline(object):
    def open_spider(self, spider):
        print("打开爬虫：", spider)
        self.session = Session()

    def process_item(self, item, spider):
        print("process item:", spider)

        if isinstance(item, MovieItem):
            movie = Movie()
            movie.name = item["name"]
            movie.icon = item["icon"]
            movie.url = item["url"]
            result = self.session.query(Movie).filter(Movie.name == item["name"]).first()
            if not result:
                self.session.add(movie)
            else:
                print("$$$$$$$$$$$$找到数据: ", result)
            print("管道中处理完成：", item)

        return item

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()