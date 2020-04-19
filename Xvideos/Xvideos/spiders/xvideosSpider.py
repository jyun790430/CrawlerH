# -*- coding: utf-8 -*-
import re
import md5
import time
import scrapy
import prettytable as pt


from Xvideos.items import XvideosItem
from scrapy.spiders import CrawlSpider
from setting.config import XVIDEOS_CATRGORY, XVIDEOS_WAIT_S_NEXT_PAGE_URL, XVIDEOS_WAIT_S_NEXT_VIDEO_URL


class Spider(CrawlSpider):

    name = 'xvideosSpider'
    domain = 'https://www.xvideos.com'
    start_urls = ['https://www.xvideos.com']

    def start_requests(self):
        for category_url in XVIDEOS_CATRGORY:
            yield scrapy.Request(url=category_url, callback=self.parse_video_page)


    def parse_video_page(self, response):
        selector = scrapy.Selector(response)

        hrefs = selector.xpath('//div[@class="thumb-under"]/p[1]/a/@href')

        for href in hrefs:
            href = self.domain + href.extract()
            time.sleep(XVIDEOS_WAIT_S_NEXT_VIDEO_URL)
            yield scrapy.Request(url=href, callback=self.parse_video_info)

        next_url = selector.xpath('//a[@class="no-page next-page"]/@href').extract()

        if next_url:
            time.sleep(XVIDEOS_WAIT_S_NEXT_PAGE_URL)
            yield scrapy.Request(url=self.domain + next_url[0], callback=self.parse_video_page)


    def parse_video_info(self, response):
        selector = scrapy.Selector(response)

        script = selector.xpath('//*[@id="video-player-bg"]/script[4]')

        video_name = re.findall('html5player\.setVideoTitle\((\'(.*?)\')\);', script.extract()[0])[0][0][1:-1]
        #video_mp4_url = re.findall('html5player\.setVideoUrlHigh\(\'(.*?)\'\);', script.extract()[0])[0]
        video_origin_url = response.url

        hash = md5.new()
        hash.update(video_origin_url.encode(encoding='utf-8'))
        video_md5_url = hash.hexdigest()

        # Get Tags
        meta_data = selector.xpath('//div[@class="video-metadata video-tags-list ordered-label-list cropped"]/ul/li/a/text()').extract()
        meta_data = meta_data[1:-1]
        video_tags = ','.join(map(str, meta_data))

        # Print Table
        tb = pt.PrettyTable()
        tb.set_style(pt.PLAIN_COLUMNS)
        tb.field_names = ["Variable", "Content"]
        tb.align["Variable"] = "l"
        tb.align["Content"] = "l"
        tb.add_row(['title', video_name])
        tb.add_row(['md5_url', video_md5_url])
        tb.add_row(['tags',  video_tags])
        tb.add_row(['origin_url', video_origin_url])

        print "\n", tb, "\n"

        item = XvideosItem()
        item['type'] = 1
        item['name'] = video_name
        item['tags'] = video_tags
        item['file_name'] = video_md5_url
        item['origin_url'] = video_origin_url
        item['unique_token'] = video_md5_url

        yield item
