# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XvideosItem(scrapy.Item):
    type = scrapy.Field()
    name = scrapy.Field()
    tags = scrapy.Field()
    file_name = scrapy.Field()
    origin_url = scrapy.Field()