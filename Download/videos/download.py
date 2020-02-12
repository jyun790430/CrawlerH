# coding=utf-8
import time
import threading


from db import conn
from parse import parse
from videos import urlconvert
from setting.config import VIDEO_FILE_PATH


class Load(threading.Thread):

    def __init__(self, queue, website, lock):
        threading.Thread.__init__(self)
        self.lock = lock
        self.queue = queue
        self.website = website

    def run(self):

        while True:
            self.lock.acquire()
            if self.queue.qsize() <= 0:

                if self.website == 'xvideos':
                    _conn = conn.db.conn()
                    cursor = _conn.cursor()
                    cursor.execute("""
                      SELECT id, origin_url, file_name FROM crawl_video WHERE TYPE = 1 and download = 0 LIMIT 6
                    """)

                    data = cursor.fetchall()

                    for k, row in enumerate(data):
                        row = list(row)
                        _url = row[1]

                        print ("x=======")
                        print _url
                        row[1] = parse.url.xvideos(_url)
                        print row[1]
                        print ("=======")

                        self.queue.put(row)


                elif self.website == 'pronhub':
                    _conn = conn.db.conn()
                    cursor = _conn.cursor()
                    cursor.execute("""
                      SELECT id, origin_url, file_name FROM crawl_video WHERE TYPE = 2 and download = 0 LIMIT 6
                    """)

                    data = cursor.fetchall()

                    for k, row in enumerate(data):
                        row = list(row)
                        _url = row[1]

                        print ("p=======")
                        print _url
                        row[1] = parse.url.pronhub(_url)
                        print row[1]
                        print ("=======")

                        self.queue.put(row)

            self.lock.release()

            if self.queue.qsize() > 0:

                # 取得 queue 的資料
                row = self.queue.get()

                url = row[1]
                file_path = VIDEO_FILE_PATH
                file_name = row[2]
                self.lock.acquire()
                print ("=======")
                print url
                print ("=======")
                self.lock.release()
                # 處理資料
                self.lock.acquire()
                print "開始下載:" + self.website + str(file_name), "\n"
                self.lock.release()
                urlconvert.mp4.store(url, file_path, file_name)
                self.lock.acquire()
                print "下載結束:" + self.website + str(file_name), "\n"
                self.lock.release()

                _conn = conn.db.conn()
                cursor = _conn.cursor()
                cursor.execute("""
                  UPDATE crawl_video SET download = 1 WHERE id = %s
                """ % row[0])
                _conn.commit()


                time.sleep(1)