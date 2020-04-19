# -*- coding: utf-8 -*-

import re
import md5
import time
import js2py
import scrapy
import prettytable as pt

from scrapy.spiders import CrawlSpider
from PronhubPremium.items import PronhubPremiumItem
from setting.config import PRONHUB_PREMIUM_CATEGORY, PRONHUB_PREMINUM_WAIT_S_NEXT_PAGE_URL, PRONHUB_PREMINUM_WAIT_S_NEXT_VIDEO_URL


class Spider(CrawlSpider):

    name = 'pronhubPremiumSpider'
    host = 'https://cn.pornhubpremium.com'
    start_urls = ['https://cn.pornhubpremium.com']

    def start_requests(self):

        for category_url in PRONHUB_PREMIUM_CATEGORY:
            yield scrapy.Request(url=category_url, callback=self.parse_video_page)


    def parse_video_page(self, response):
        selector = scrapy.Selector(response)

        divs = selector.xpath('//div[@class="phimage"]')
        for div in divs:

            viewkey = re.findall('viewkey=(.*?)"', div.extract())
            time.sleep(PRONHUB_PREMINUM_WAIT_S_NEXT_VIDEO_URL)
            yield scrapy.Request(url='https://cn.pornhubpremium.com/view_video.php?viewkey=%s' % viewkey[0], callback=self.parse_video_info)


        url_next = selector.xpath('//li[@class="page_next"]/a/@href').extract()
        url_next2 = selector.xpath('//div[@class="greyButton page_next"]/a/@href').extract()

        url_next = url_next if url_next else url_next2

        # Prevent 429 Status
        time.sleep(PRONHUB_PREMINUM_WAIT_S_NEXT_PAGE_URL)

        if url_next:
            yield scrapy.Request(url=self.host + url_next[0], callback=self.parse_video_page)


    def parse_video_info(self, response):

        selector = scrapy.Selector(response)

        script = selector.xpath('//script/text()').extract()
        for j in script:

            if 'flashvars' in j:

                video_origin_url = response.url

                hash = md5.new()
                hash.update(video_origin_url.encode(encoding='utf-8'))
                video_md5_url = hash.hexdigest()

                video_name = selector.xpath('//div[@id="main-container"]/@data-video-title').extract()
                #video_name = selector.xpath('//div[@class="videoTitle"]/span/text()').extract()
                if not video_name :
                    video_name = selector.xpath('//div[@class="headerWrap clearfix"]/h1/span/text()').extract()

                if video_name:
                    video_name = video_name[0]
                else:
                    print selector.extract()

                categories = selector.xpath('//div[@class="categoriesWrapper"]/a/text()').extract()
                tags = selector.xpath('//div[@class="tagsWrapper"]/a/text()').extract()

                if not tags :

                    tags = selector.xpath('//div[@class="tags floatLeft"]/a[@class="js-mxp"]/text()').extract()
                    categories = selector.xpath('//div[@class="tags floatLeft"]/a/text()').extract()
                    categories = categories[(len(tags)):(len(categories))]

                video_tags = ','.join([unicode(x.decode('utf-8')) if type(x) == type(str()) else unicode(x) for x in tags])
                video_categories = ','.join([unicode(x.decode('utf-8')) if type(x) == type(str()) else unicode(x) for x in categories])


                # Print Table
                tb = pt.PrettyTable()
                tb.field_names = ["Variable", "Content"]
                tb.align["Variable"] = "l"
                tb.align["Content"] = "l"
                tb.add_row(['title', video_name])
                tb.add_row(['md5_url', video_md5_url])
                tb.add_row(['tags', video_tags])
                tb.add_row(['categories', video_categories])
                tb.add_row(['origin_url', video_origin_url])

                print "\n", tb, "\n"

                item = PronhubPremiumItem()
                item['type'] = 3
                item['name'] = video_name
                item['tags'] = video_tags
                item['file_name'] = video_md5_url
                item['origin_url'] = video_origin_url
                item['categories'] = video_categories
                item['unique_token'] = video_md5_url

                yield item






        # _video_info = re.findall('var flashvars =(.*?}),\n|var flashvars =(.*?});', selector.extract())
        #
        # if len(_video_info) <= 0:
        #     logging.debug('==================================')
        #     logging.debug('Url Can\'t Parse: ' + response.url)
        #     logging.debug('==================================')
        #     return
        # else:
        #     _video_info = _video_info[0]
        #
        # __video_json = {}
        #
        # for _parse_str in _video_info:
        #     if _parse_str.strip():
        #         __video_json = json.loads(_parse_str)
        #
        # title     = __video_json.get('video_title')
        # link_url  = __video_json.get('link_url')
        # image_url = __video_json.get('image_url')
        # duration  = __video_json.get('video_duration')
        #
        # _video_mp4480 = re.findall('var mp4480p=(.*?);', selector.extract())
        # _video_mp4480_item = re.sub('(\/\*[^\*]*?\*\/)?', "", _video_mp4480[0])  # 濾掉 Comment
        # _video_mp4480_item = [_item.strip() for _item in _video_mp4480_item.split('+')]
        #
        # _url = ''
        # for _variable in _video_mp4480_item:
        #     _variable = re.findall('var %s="(.*?)";' % _variable, selector.extract())[0]
        #     _variable = re.sub('([+\s"])', "", _variable)
        #     _url += _variable
        #
        # print('===========')
        # print(title)
        # print(link_url)
        # print(image_url)
        # print(duration)
        # print(_url)
        # print('===========')



        # phItem['video_duration'] = duration
        #
        # phItem['video_title'] = title
        # image_url = _ph_info_json.get('image_url')
        # phItem['image_url'] = image_url
        # link_url = _ph_info_json.get('link_url')
        # phItem['link_url'] = link_url
        # phItem['quality_480p'] = quality_480p
        # logging.info('duration:' + duration + ' title:' + title + ' image_url:'
        #              + image_url + ' link_url:' + link_url)
        # yield phItem
