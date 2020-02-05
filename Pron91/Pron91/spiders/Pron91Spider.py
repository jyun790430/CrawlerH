# -*- coding: utf-8 -*-
import re
import js2py
import scrapy

from pyv8 import PyV8


class Pron91spiderSpider(scrapy.Spider):
    name = 'Pron91Spider'
    start_urls = ['http://www.91porn.com/index.php']

    def start_requests(self):
        yield scrapy.Request(url='http://www.91porn.com/v.php?next=watch', callback=self.parse_video_page)


    def parse_video_page(self, response):
        selector = scrapy.Selector(response)

        hrefs = selector.xpath('//div[@class="listchannel"]/div[1]/a/@href')

        for href in hrefs:
            href = href.extract()
            yield scrapy.Request(url=href, callback=self.parse_video_info)


    def parse_video_info(self, response):
        selector = scrapy.Selector(response)

        script = selector.xpath('//div[@class="media-parent"]/div/video/script')

        params = re.findall('strencode\((.*)\)', script.extract()[0])[0]
        params = params.split(',')

        js = u"""
        
            function strencode(input, key)
            {
                input = atob(input);
                len = key.length;
                code = '';
                for (i = 0; i < input.length; i++) {
                    k = i %% len;
                    code += String.fromCharCode(input.charCodeAt(i) ^ key.charCodeAt(k));
                }
                return atob(code);
            }
            
            let source = strencode(%s, %s)
        """ % (params[0], params[1])

        # JS ENCODE CONVERT PYTHON
        # def aencode(self, input, key):
        #     input = input.decode('base64')
        #     _len = len(key)
        #
        #     code = ''
        #     for i in range(_len):
        #         _key = i % _len
        #
        #         code += chr(ord(input[i]) ^ ord(key[_key]))
        #
        #     return code.decode('base64')

        ctxt = PyV8.JSContext()
        ctxt.enter()

        ctxt.eval(js)
        vars = ctxt.locals
        print(vars.source)

