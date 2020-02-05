# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

from scrapy import Item
from Xvideos import settings


class XvideosPipeline(object):


    def __init__(self):
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.connect.cursor()


    def process_item(self, item, spider):
        _sql = """
            INSERT INTO xvideos (video_title, video_url) 
            VALUES (\"%s\", \"%s\")
        """ % (
            item['video_title'], item['video_url']
        )

        self.cursor.execute(_sql)
        self.connect.commit()

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



#
# # -*- coding: utf-8 -*-
#
# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#
# import pymongo
# from pymongo import IndexModel, ASCENDING
# from items import PornVideoItem
#
#
# class PornhubMongoDBPipeline(object):
#     def __init__(self):
#         clinet = pymongo.MongoClient("localhost", 27017)
#         db = clinet["PornHub"]
#         self.PhRes = db["PhRes"]
#         idx = IndexModel([('link_url', ASCENDING)], unique=True)
#         self.PhRes.create_indexes([idx])
#         # if your existing DB has duplicate records, refer to:
#         # https://stackoverflow.com/questions/35707496/remove-duplicate-in-mongodb/35711737
#
#     def process_item(self, item, spider):
#         print 'MongoDBItem', item
#         """ 判断类型 存入MongoDB """
#         if isinstance(item, PornVideoItem):
#             print 'PornVideoItem True'
#             try:
#                 self.PhRes.update_one({'link_url': item['link_url']}, {'$set': dict(item)}, upsert=True)
#             except Exception:
#                 pass
#         return item
