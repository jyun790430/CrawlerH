# -*- coding: utf-8 -*-
import re
import scrapy

from Xvideos.items import XvideosItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class XvideosspiderSpider(CrawlSpider):
    name = 'xvideosSpider'
    domain = 'https://www.xvideos.com'
    start_urls = ['https://www.xvideos.com']

    def start_requests(self):
        yield scrapy.Request(url='https://www.xvideos.com', callback=self.parse_video_page)


    def parse_video_page(self, response):
        selector = scrapy.Selector(response)

        hrefs = selector.xpath('//div[@class="thumb-under"]/p[1]/a/@href')

        for href in hrefs:
            href = self.domain + href.extract()
            yield scrapy.Request(url=href, callback=self.parse_video_info)

        next_url = selector.xpath('//a[@class="no-page next-page"]/@href').extract()

        if next_url:
            yield scrapy.Request(url=self.domain + next_url[0], callback=self.parse_video_page)


    def parse_video_info(self, response):
        selector = scrapy.Selector(response)

        script = selector.xpath('//*[@id="video-player-bg"]/script[4]')

        _url = re.findall('html5player\.setVideoUrlHigh\(\'(.*?)\'\);', script.extract()[0])[0]
        _referer = response.request.headers.get('Referer', None)
        print("------------------------------")
        print(_referer)
        print(_url)
        print("------------------------------")

        item = XvideosItem()
        item['video_url'] = _url
        item['video_title'] = 'haha'

        yield item
