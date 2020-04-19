# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

from scrapy import Item
from setting.config import MYSQL_CONN


class XvideosPipeline(object):

    def __init__(self):
        self.connect = pymysql.connect(
            host=MYSQL_CONN['host'],
            db=MYSQL_CONN['db'],
            user=MYSQL_CONN['user'],
            passwd=MYSQL_CONN['passwd'],
            port=MYSQL_CONN['port'],
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.connect.cursor()


    def process_item(self, item, spider):
        _sql = """
            INSERT INTO crawl_video (type, name, tags, file_name, origin_url, unique_token) 
            VALUES (\"%s\", \"%s\",\"%s\", \"%s\",\"%s\",\"%s\")
        """ % (
            item['type'], item['name'], item['tags'], item['file_name'], item['origin_url'], item['unique_token']
        )
        try:
            self.cursor.execute(_sql)
            self.connect.commit()
        except:
            pass

        return ''

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()

    # Mongo Setting
    #@classmethod
    # def from_crawler(cls, crawler):
    #     cls.DB_URL = crawler.settings.get('MONGO_DB_URI', 'mongodb://localhost:27017')
    #     cls.DB_NAME = crawler.settings.get('MONGO_DB_NAME', 'xvideos')
    #
    #     return cls()
    #
    #
    # def open_spider(self, spider):
    #     self.client = pymongo.MongoClient(self.DB_URL)
    #     self.db = self.client[self.DB_NAME]
    #
    #
    # def close_spider(self, spider):
    #     self.client.close()
    #
    #
    # def process_item(self, item, spider):
    #     collection = self.db[spider.name]
    #     post = dict(item) if isinstance(item, Item) else item
    #     collection.insert_one(post)
    #     return item