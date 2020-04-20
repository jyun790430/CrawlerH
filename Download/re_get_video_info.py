# coding=utf-8

import os
import time

from model import conn
from setting.config import VIDEO_FILE_PATH

from videos import urlparse

files = os.listdir(VIDEO_FILE_PATH)

type = 1

def getVideo(type):
    _conn = conn.db.conn()
    cursor = _conn.cursor()
    sql = """
            select id, origin_url from crawl_video 
            where duration is null and type = %s
    """ % (type)
    cursor.execute(sql)
    data = cursor.fetchall()
    _conn.close()

    return data


def updateDuration(id, sec):
    _conn = conn.db.conn()
    cursor = _conn.cursor()
    sql = """
        update crawl_video set duration = %s where id = %s
    """ % (sec, id)
    print sql
    cursor.execute(sql)
    _conn.commit()
    _conn.close()


data = getVideo(type)

for k, row in enumerate(data):
    id = row[0]
    url = row[1]

    if type == 1:
        data = urlparse.Url.xvideos(url)
    if type == 2:
        data = urlparse.Url.pronhub(url)
        time.sleep(2)
    if type == 3:
        data = urlparse.Url.pronhubPremium(url)
        time.sleep(2)

    _duration = int(data['duration'])
    updateDuration(id, _duration)

# for _f in data:
#
#
#     print '========================================'
#     _f = _f.replace(".mp4", "")
#     _f = _f.replace(" ", "")
#     _f = str(_f.strip())
#     print out, _f
#
#     _conn = conn.db.conn()
#     cursor = _conn.cursor()
#
#     if not out:
#         continue
#
#     sql = """
#         update crawl_video set duration = %s where unique_token = "%s"
#     """ % (out, _f)
#
#     try:
#         cursor.execute(sql)
#         _conn.commit()
#         _conn.close()
#     except:
#         pass