# coding=utf-8

import re
import js2py
import requests


from lxml import html
from videos import  urlparse

# import Queue as queue
#
# _queue = queue.PriorityQueue()
# _queue.put(1)
# _queue.put(2)
#
# print(list(_queue))
# print _queue.get()


#print urlparse.Url.xvideos("https://www.xvideos.com/video52408443/_")
print urlparse.Url.pronhub("https://www.pornhub.com/view_video.php?viewkey=ph5dc1cbb37d577")
#print urlparse.Url.pronhubPremium("https://www.pornhubpremium.com/view_video.php?viewkey=863826900")


#url = "https://www.w3school.com.cn/xpath/xpath_nodes.asp"
# response = requests.get(url)
# selector = html.fromstring(response.text)
#
# div = selector.xpath('//div[@id="course"]')
#
# print response.text
# print div
# print div[0].text