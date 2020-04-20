# -*- coding: utf-8 -*-

import re
import json
import js2py
import random
import requests
import prettytable as pt


from lxml import html
from videos.user_agents import agents
from setting.config import XVIDEOS_COOKIE, PRONHUB_PREMIUM_COOKIE


class Url:

    @staticmethod
    def pronhub(url):

        headers = Url.getUserAgent()
        cookies = Url.pronHubCookie()
        response = requests.get(url, headers=headers, cookies=cookies)
        selector = html.fromstring(response.text)

        script = selector.xpath('//script/text()')

        for j in script:

            if 'flashvars' in j:

                duration = 0
                durationContent = selector.xpath('//meta[@property="video:duration"]/@content')
                if durationContent:
                    duration = int(durationContent[0])

                qualityItems = re.findall('qualityItems_\d+', j)

                if len(qualityItems) <= 0:
                    # Print Error
                    tb = pt.PrettyTable()
                    tb.title = "Url Parse Error"
                    tb.field_names = ["Website", "Url"]
                    tb.align["Url"] = "l"
                    tb.align["Website"] = "l"
                    tb.add_row(["pronhub", response.url])
                    print "\n", tb, "\n"
                    return
                else:
                    _video_url = qualityItems[0]

                js_split = j.split('\n')

                js = ''
                for _str in js_split:
                    if 'playerObjList' in _str or 'embedId' in _str or 'embedSWF' in _str:
                        continue

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
                        #p = _dict['text']
                        url = _dict['url']
                        break

                return {
                    'url': url,
                    'duration': duration
                }

        return None


    @staticmethod
    def pronhubPremium(url):

        headers = Url.getUserAgent()
        cookies = Url.pronHubPremiumCookie()
        response = requests.get(url, headers=headers, cookies=cookies)
        selector = html.fromstring(response.text)

        script = selector.xpath('//script/text()')

        for j in script:

            if 'flashvars' in j:

                duration = 0
                durationContent = selector.xpath('//meta[@property="video:duration"]/@content')
                if durationContent:
                    duration = int(durationContent[0])

                script = selector.xpath('//meta[@id="video-player-bg"]/script[4]')

                qualityItems = re.findall('qualityItems_\d+', j)

                if len(qualityItems) <= 0:
                    # Print Error
                    tb = pt.PrettyTable()
                    tb.title = "Url Parse Error"
                    tb.field_names = ["Website", "Url"]
                    tb.align["Url"] = "l"
                    tb.align["Website"] = "l"
                    tb.add_row(["pronhub", response.url])
                    print "\n", tb, "\n"
                    return
                else:
                    _video_url = qualityItems[0]

                js_split = j.split('\n')

                js = ''

                for _str in js_split:
                    if 'playerObjList' in _str or 'embedId' in _str or 'embedSWF' in _str:
                        continue

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
                        # p = _dict['text']
                        url = _dict['url']
                        break

                return {
                    'url': url,
                    'duration': duration
                }

        return None


    @staticmethod
    def xvideos(url):

        cookies = Url.xvideosCookie()
        response = requests.get(url, cookies=cookies)
        selector = html.fromstring(response.text)

        script = selector.xpath('//*[@id="video-player-bg"]/script[4]')

        duration = 0
        duration_string = selector.xpath('//h2[@class="page-title"]/span/text()')

        if duration_string:
            duration_string = duration_string[0].split()
            _dsec = 0
            for d in duration_string:
                if str.isdigit(d):
                    _dsec = int(d)
                    continue

                switcher = {
                    'h': 60 * 60,
                    'min': 60,
                    'sec': 1
                }
                _sec = switcher.get(d, None)
                if _sec:
                    duration += _dsec * _sec


        if len(script) <= 0:
            # Print Error
            tb = pt.PrettyTable()
            tb.title = "Url Parse Error"
            tb.field_names = ["Website", "Url"]
            tb.align["Url"] = "l"
            tb.align["Website"] = "l"
            tb.add_row(["xvideos", response.url])
            print "\n", tb, "\n"
            return None

        _url = re.findall('html5player\.setVideoUrlHigh\(\'(.*?)\'\);', script[0].text)
        _url = _url[0] if len(_url) > 0 else None

        return {
            'url': _url,
            'duration': duration
        }


    @staticmethod
    def getUserAgent():
        agent = random.choice(agents)
        headers = dict()
        headers["User-Agent"] = agent

        return headers


    @staticmethod
    def xvideosCookie():
        cookie = {
            'session_token': XVIDEOS_COOKIE
        }

        _cookie = json.dumps(cookie)

        return json.loads(_cookie)


    @staticmethod
    def pronHubCookie():
        cookie = {
            'platform': 'pc',
            'ss': '367701188698225489',
            'bs': '%s',
            'RNLBSERVERID': 'ded6699',
            'FastPopSessionRequestNumber': '1',
            'FPSRN': '1',
            'performance_timing': 'home',
            'RNKEY': '40859743*68067497:1190152786:3363277230:1'
        }

        bs = ''
        for i in range(32):
            bs += chr(random.randint(97, 122))
        _cookie = json.dumps(cookie) % bs

        return json.loads(_cookie)


    @staticmethod
    def pronHubPremiumCookie():
        cookie = {
            'platform': 'pc',
            'ss': '367701188698225489',
            'bs': '%s',
            'RNLBSERVERID': 'ded6699',
            'FastPopSessionRequestNumber': '1',
            'FPSRN': '1',
            'performance_timing': 'home',
            'RNKEY': '40859743*68067497:1190152786:3363277230:1',
            'il': PRONHUB_PREMIUM_COOKIE,
        }

        bs = ''
        for i in range(32):
            bs += chr(random.randint(97, 122))
        _cookie = json.dumps(cookie) % bs

        return json.loads(_cookie)



