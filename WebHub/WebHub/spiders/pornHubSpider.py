#coding:utf-8
import re
import json
import logging

from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider
from WebHub.pornhub_type import PH_TYPES
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class Spider(CrawlSpider):
    name = 'pornHubSpider'
    host = 'https://www.pornhub.com'
    start_urls = list(set(PH_TYPES))
    logging.getLogger("requests").setLevel(logging.WARNING)  # 将requests的日志级别设成WARNING
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename='cataline.log',
        filemode='w')


    def start_requests(self):
        for ph_type in self.start_urls:
            yield Request(url='https://www.pornhub.com/%s' % ph_type, callback=self.parse_ph_key)


    def parse_ph_key(self, response):
        selector = Selector(response)
        logging.debug('request url:------>' + response.url)
        # logging.info(selector)


        #yield Request(url='https://www.pornhub.com/embed/ph5df50e070e7c5', callback=self.parse_video_info)

        divs = selector.xpath('//div[@class="phimage"]')
        for div in divs:
            # logging.debug('divs :------>' + div.extract())

            viewkey = re.findall('viewkey=(.*?)"', div.extract())
            # logging.debug(viewkey)
            yield Request(url='https://www.pornhub.com/embed/%s' % viewkey[0], callback=self.parse_video_info)


        url_next = selector.xpath(
            '//a[@class="orangeButton" and text()="Next "]/@href').extract()
        logging.debug(url_next)
        if url_next:
            # if self.test:
            logging.debug(' next page:---------->' + self.host + url_next[0])
            yield Request(url=self.host + url_next[0],
                          callback=self.parse_ph_key)
            self.test = False


    def parse_video_info(self, response):
        #phItem = PornVideoItem()

        selector = Selector(response)
        #logging.info(selector)

        _video_info = re.findall('var flashvars =(.*?}),\n|var flashvars =(.*?});', selector.extract())

        if len(_video_info) <= 0:
            logging.debug('==================================')
            logging.debug('Url Can\'t Parse: ' + response.url)
            logging.debug('==================================')
            return
        else:
            _video_info = _video_info[0]

        __video_json = {}

        for _parse_str in _video_info:
            if _parse_str.strip():
                __video_json = json.loads(_parse_str)

        title     = __video_json.get('video_title')
        link_url  = __video_json.get('link_url')
        image_url = __video_json.get('image_url')
        duration  = __video_json.get('video_duration')

        _video_mp4480 = re.findall('var mp4480p=(.*?);', selector.extract())
        _video_mp4480_item = re.sub('(\/\*[^\*]*?\*\/)?', "", _video_mp4480[0])  # 濾掉 Comment
        _video_mp4480_item = [_item.strip() for _item in _video_mp4480_item.split('+')]

        _url = ''
        for _variable in _video_mp4480_item:
            _variable = re.findall('var %s="(.*?)";' % _variable, selector.extract())[0]
            _variable = re.sub('([+\s"])', "", _variable)
            _url += _variable

        print('===========')
        print(title)
        print(link_url)
        print(image_url)
        print(duration)
        print(_url)
        print('===========')



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
