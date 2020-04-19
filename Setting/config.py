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

PRONHUB_PREMIUM_CATEGORY = [
	'https://cn.pornhubpremium.com/video?c=111&hd=1&premium=1'
]

XVIDEOS_CATRGORY = [
    "https://www.xvideos.com/best/2020-01",
    "https://www.xvideos.com/best/2019-12"
]

VIDEO_FILE_PATH = "/Users/bryson/videoH"

### Server ID
SERVER_ID = 0

### Thread
THREAD_NUM_XVIDEOX = 1
THREAD_NUM_PRONHUB = 1
THREAD_NUM_PRONHUB_PREMIUM = 1

### Spider Xvideos
XVIDEOS_WAIT_S_NEXT_PAGE_URL  = 0
XVIDEOS_WAIT_S_NEXT_VIDEO_URL = 0

### Spider Pronhub
PRONHUB_WAIT_S_NEXT_PAGE_URL  = 4
PRONHUB_WAIT_S_NEXT_VIDEO_URL = 30

### Spider Pronhub Preminum
PRONHUB_PREMINUM_WAIT_S_NEXT_PAGE_URL  = 4
PRONHUB_PREMINUM_WAIT_S_NEXT_VIDEO_URL = 30


### Download video, wait second to next
XVIDEOS_WAIT_S_NEXT_DOWNLOAD = 20
PRONHUB_WAIT_S_NEXT_DOWNLOAD = 60
PRONHUB_PREMINUM_WAIT_S_NEXT_DOWNLOAD = 60


### Cookie
XVIDEOS_COOKIE = "f1403e7e43a3759dsd8VC07olgiro3pnojtnuaayu13qsS7UkSm5QNdHkVdUC12I23K2bkXZtELu_lr7KMfMaXsPOP8HNLVsgSdZrscRC9gdGIhhSevZctyq31QiKNY-yP2XAC3_K5ofbw_rmbhawtBByNKCjsEddnfItYNB-BV-OhJLRawaeVIVh_FF5bUa-xbBBjP59agkj9Cp5mQNKfWKCxx2e_prj-YQFyFoY_CQgkdnv2OV6SF2Xdg%3D"
PRONHUB_PREMIUM_COOKIE = "v1Uo81aOoMAF0Hy-bBWsqx7eDaLS5-jHQpCp1kQF9GTIExNTg3MjgzNTM4bzJVVEVGd1o2bTl0NG9ydTFGZmdsOG9iVEVJX0ZJMTlJem1hN2Z4TA.."

