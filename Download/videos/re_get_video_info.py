# coding=utf-8

import time

import requests
from lxml import html

from model  import CrawlVideoModel
from videos.urlparse import Url


class reVideo():

    def run(self):

        data = CrawlVideoModel.Objects.getVedioDetail(2, 0)

        for k, row in enumerate(data):
            row = list(row)
            id = row[0]
            _url = row[1]
            _url = _url.replace("www", "cn")

            time.sleep(3)

            headers = Url.getUserAgent()
            cookies = Url.pronHubPremiumCookie()
            response = requests.get(_url, headers=headers, cookies=cookies)
            selector = html.fromstring(response.text)

            script = selector.xpath('//script/text()')

            for j in script:
                if 'flashvars' in j:

                    categories = selector.xpath('//div[@class="categoriesWrapper"]/a/text()')
                    tags = selector.xpath('//div[@class="tagsWrapper"]/a/text()')

                    if not tags:
                        tags = selector.xpath('//div[@class="tags floatLeft"]/a[@class="js-mxp"]/text()')
                        categories = selector.xpath('//div[@class="tags floatLeft"]/a/text()')
                        categories = categories[(len(tags)):(len(categories))]

                    video_tags = ','.join(
                        [unicode(x.decode('utf-8')) if type(x) == type(str()) else unicode(x) for x in tags])
                    video_categories = ','.join(
                        [unicode(x.decode('utf-8')) if type(x) == type(str()) else unicode(x) for x in categories])

                    print video_tags
                    print video_categories

                    CrawlVideoModel.Objects.reUpdateDetail(id, 1, video_tags, video_categories)

