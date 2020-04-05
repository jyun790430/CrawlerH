# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql

from scrapy import Item
from setting.config import MYSQL_CONN

class PronhubPremiumPipeline(object):

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
            INSERT INTO crawl_video (type, name, tags, categories, file_name, origin_url) 
            VALUES (\"%s\", \"%s\",\"%s\", \"%s\",\"%s\",\"%s\")
        """ % (
            item['type'], item['name'], item['tags'], item['categories'], item['file_name'], item['origin_url']
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
