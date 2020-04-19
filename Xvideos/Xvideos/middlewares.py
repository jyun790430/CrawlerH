# encoding=utf-8
import json
import random
from setting.config import XVIDEOS_COOKIE

class CookiesMiddleware(object):
    """ 换Cookie """
    cookie = {
        'session_token': XVIDEOS_COOKIE
    }

    def process_request(self, request, spider):
        _cookie = json.dumps(self.cookie)
        request.cookies = json.loads(_cookie)
