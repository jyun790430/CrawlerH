# -*- coding: utf-8 -*-
import re
import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class XvideosspiderSpider(CrawlSpider):
    name = 'xvideosSpider'
    domain = 'https://www.xvideos.com'
    start_urls = ['https://www.xvideos.com']

    rules = (
        # 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
        Rule(LinkExtractor(allow=('/new/')), callback='parse_video_page'),
    )

    # def start_requests(self):
    #     yield scrapy.Request(url='https://www.xvideos.com', callback=self.parse_video_page)


    def parse_video_page(self, response):
        selector = scrapy.Selector(response)

        hrefs = selector.xpath('//div[@class="thumb-under"]/p[1]/a/@href')

        for href in hrefs:
            href = self.domain + href.extract()
            yield scrapy.Request(url=href, callback=self.parse_video_info)


    def parse_video_info(self, response):
        selector = scrapy.Selector(response)

        script = selector.xpath('//*[@id="video-player-bg"]/script[4]')

        _url = re.findall('html5player\.setVideoUrlHigh\(\'(.*?)\'\);', script.extract()[0])[0]
        _referer = response.request.headers.get('Referer', None)
        print("------------------------------")
        print(_referer)
        print(_url)
        print("------------------------------")
