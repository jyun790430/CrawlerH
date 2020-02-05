# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XvideosItem(scrapy.Item):
    # define the fields for your item here like:
    video_url = scrapy.Field()
    video_title = scrapy.Field()
    pass
