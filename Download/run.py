# coding=utf-8

import Queue as queue

from videos import download
from videos import urlconvert
from db import conn

import pymysql

cursor = conn.db.cursor()
cursor.execute("SELECT * FROM xvideos")
a = cursor.fetchall()

for x in a:
  print(x)

mp4List = [
    "https://vid1-l3.xvideos-cdn.com/videos/mp4/6/c/f/xvideos.com_6cfb6efd81a04b5c6b9b98026d617b3f-1.mp4?e=1581403474&ri=1024&rs=85&h=96ae93a493a40cd526d3f6da4e87485c",
    "https://vid3-l3.xvideos-cdn.com/videos/mp4/2/a/9/xvideos.com_2a921afe792dc721731f8b2624007162.mp4?e=1581403474&ri=1024&rs=85&h=dfd842470403efd1cdea38be0ca241cc",
    "https://video-hw.xvideos-cdn.com/videos/mp4/0/4/a/xvideos.com_04a6f5166a6bb250cf2408edb42511ac-1.mp4?e=1581403474&ri=1024&rs=85&h=50a31a4a724517de2be404b05262f644",
    "https://vid2-l3.xvideos-cdn.com/videos/mp4/7/c/4/xvideos.com_7c49c6e7ba600677f531932afc80a156.mp4?e=1581403474&ri=1024&rs=85&h=32274f8d46033aae501f4d48a2f29dd3",
    "https://vid2-l3.xvideos-cdn.com/videos/mp4/e/3/a/xvideos.com_e3a0c42aab62263468db641c2a9b81e8-1.mp4?e=1581403474&ri=1024&rs=85&h=c63ded8bb2af6125f8b2084a5232e84c"
]

#print conn.db.cursor().cursor().execute("SHOW TABLES").fetchall()
#a = conn.db.cursor().execute("SELECT * FROM xvideos").fetchall()
# for x in a:
#   print(x)

# _queue = queue.Queue()
#
# # 將資料放入佇列
# for i in mp4List:
#     _queue.put(i)
#
# # 建立兩個 Worker
# my_worker1 = download.Load(_queue, 1)
# my_worker2 = download.Load(_queue, 2)
# my_worker3 = download.Load(_queue, 3)
#
# # 讓 Worker 開始處理資料
# my_worker1.start()
# my_worker2.start()
# my_worker3.start()
#
# # 等待所有 Worker 結束
# my_worker1.join()
# my_worker2.join()
# my_worker3.join()
