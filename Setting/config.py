#coding:utf-8

MYSQL_CONN = {
    'host' : '127.0.0.1',
    'db': 'crawlh',
    'user': 'root',
    'passwd': 'root',
    'port': 3306
}

PRONHUB_CATEGORY = [
    'https://cn.pornhub.com/video/search?search=%E7%A0%B4%E8%A7%A3'
]

PRONHUBPREMIUM_CATEGORY = [
	'https://cn.pornhubpremium.com/video?c=111&hd=1&premium=1'
]

XVIDEOS_CATRGORY = [
    "https://www.xvideos.com/best/2020-01",
    "https://www.xvideos.com/best/2019-12"
]

VIDEO_FILE_PATH = "/Users/bryson/videoH"

THREAD_NUM = 5

THREAD_NUM_XVIDEOX = 5
THREAD_NUM_PRONHUB = 3
THREAD_NUM_PRONHUB_PREMIUM = 2