# coding=utf-8

import time
import datetime
import threading


from model  import CrawlVideoModel
from videos import urlparse, mp4converter
from setting.config import VIDEO_FILE_PATH, THREAD_NUM_XVIDEOX, THREAD_NUM_PRONHUB, THREAD_NUM_PRONHUB_PREMIUM, XVIDEOS_WAIT_S_NEXT_DOWNLOAD, PRONHUB_WAIT_S_NEXT_DOWNLOAD, PRONHUB_PREMINUM_WAIT_S_NEXT_DOWNLOAD


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

                    data = CrawlVideoModel.Objects.getUnDoneDetail(1, THREAD_NUM_XVIDEOX)

                    for k, row in enumerate(data):
                        row = list(row)
                        _url = row[1]
                        data = urlparse.Url.xvideos(_url)
                        row[1] = data['url']
                        print row

                        CrawlVideoModel.Objects.updateDetail(row[0], 0, 3)

                        self.queue.put(row)

                    if not data:
                        print 'stop'
                        break


                elif self.website == 'pronhub':

                    data = CrawlVideoModel.Objects.getUnDoneDetail(2, THREAD_NUM_PRONHUB)

                    for k, row in enumerate(data):
                        row = list(row)
                        _url = row[1]
                        data = urlparse.Url.pronhub(_url)
                        row[1] = data['url']
                        print row

                        CrawlVideoModel.Objects.updateDetail(row[0], 0, 3)

                        self.queue.put(row)

                    if not data:
                        print 'stop'
                        break

                elif self.website == 'pronhubPremium':

                    data = CrawlVideoModel.Objects.getUnDoneDetail(3, THREAD_NUM_PRONHUB_PREMIUM)

                    for k, row in enumerate(data):
                        row = list(row)
                        _url = row[1]
                        data = urlparse.Url.pronhubPremium(_url)
                        row[1] = data['url']
                        print row

                        CrawlVideoModel.Objects.updateDetail(row[0], 0, 3)

                        self.queue.put(row)

                    if not data:
                        print 'stop'
                        break

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
                        CrawlVideoModel.Objects.updateDetail(row[0], 1, 0, res['fileName'])
                    else:
                        CrawlVideoModel.Objects.updateDetail(row[0], 0, 2)
                else:
                    CrawlVideoModel.Objects.updateDetail(row[0], 0, 1)

                if self.website == 'xvideos':
                    time.sleep(XVIDEOS_WAIT_S_NEXT_DOWNLOAD)
                elif self.website == 'pronhub':
                    time.sleep(XVIDEOS_WAIT_S_NEXT_DOWNLOAD)
                elif self.website == 'pronhubPremium':
                    time.sleep(PRONHUB_PREMINUM_WAIT_S_NEXT_DOWNLOAD)

    def _print(self, text):
        self.lock.acquire()
        print text
        self.lock.release()

