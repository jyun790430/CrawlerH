# -*- coding: utf-8 -*-

import re
import js2py
import requests

from lxml import html

class url:

    @staticmethod
    def pronhub(url):
        response = requests.get(url)
        selector = html.fromstring(response.text)

        script = selector.xpath('//script/text()')

        for j in script:

            if 'flashvars' in j:

                qualityItems = re.findall('qualityItems_\d+', j)

                if len(qualityItems) <= 0:
                    logging.debug('==================================')
                    logging.debug('Url Can\'t Parse: ' + response.url)
                    logging.debug('==================================')
                    return
                else:
                    _video_url = qualityItems[0]

                js_split = j.split('\n')

                js = ''
                for _str in js_split:
                    if 'loadScript' in _str:
                        if _video_url in _str:
                            _str = re.sub(r'(loadScript.*)', '', _str)
                            js += _str
                        break
                    else:
                        js += _str

                js = js + _video_url

                res = js2py.eval_js(js)

                if not type(res) is js2py.base.JsObjectWrapper:
                    res = json.loads(str(res))
                else:
                    res = list(res)

                url = ''
                for _dict in reversed(res):
                    if not _dict['url']:
                        continue
                    else:
                        p = _dict['text']
                        url = _dict['url']
                        break

                return url


    @staticmethod
    def xvideos(url):
        response = requests.get(url)
        selector = html.fromstring(response.text)

        script = selector.xpath('//*[@id="video-player-bg"]/script[4]')
        _url = re.findall('html5player\.setVideoUrlHigh\(\'(.*?)\'\);', script[0].text)[0]

        return _url


