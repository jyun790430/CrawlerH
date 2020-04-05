# coding=utf-8

import time
import datetime
import threading


from model  import CrawlVideoModel
from videos import urlparse, mp4converter
from setting.config import VIDEO_FILE_PATH, THREAD_NUM


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

                    data = CrawlVideoModel.Objects.getUnDoneDetail(1, THREAD_NUM)

                    for k, row in enumerate(data):
                        row = list(row)
                        _url = row[1]
                        row[1] = urlparse.Url.xvideos(_url)

                        CrawlVideoModel.Objects.updateDetail(row[0], 0, 3)

                        self.queue.put(row)


                elif self.website == 'pronhub':

                    data = CrawlVideoModel.Objects.getUnDoneDetail(2, THREAD_NUM)

                    for k, row in enumerate(data):
                        row = list(row)
                        _url = row[1]
                        row[1] = urlparse.Url.pronhub(_url)

                        CrawlVideoModel.Objects.updateDetail(row[0], 0, 3)

                        self.queue.put(row)

                elif self.website == 'pronhubPremium':

                    data = CrawlVideoModel.Objects.getUnDoneDetail(3, THREAD_NUM)

                    for k, row in enumerate(data):
                        row = list(row)
                        _url = row[1]
                        row[1] = urlparse.Url.pronhubPremium(_url)

                        CrawlVideoModel.Objects.updateDetail(row[0], 0, 3)

                        self.queue.put(row)

            self.lock.release()

            if self.queue.qsize() > 0:

                # 取得 queue 的資料
                row = self.queue.get()

                url = row[1]
                file_name = row[2]
                file_path = VIDEO_FILE_PATH

                if url:
                    # 處理資料
                    self._print("[%s] %s_開始下載: %s.mp4" % (datetime.datetime.now(), self.website, str(file_name)))
                    res = mp4converter.mp4.store(url, file_path, file_name)
                    self._print("[%s] %s_下載結束: %s.mp4" % (datetime.datetime.now(), self.website, str(file_name)))

                    if res:
                        CrawlVideoModel.Objects.updateDetail(row[0], 1, 0)
                    else:
                        CrawlVideoModel.Objects.updateDetail(row[0], 0, 2)
                else:
                    CrawlVideoModel.Objects.updateDetail(row[0], 0, 1)

                time.sleep(1)

    def _print(self, text):
        self.lock.acquire()
        print text
        self.lock.release()

