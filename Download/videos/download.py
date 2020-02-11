# coding=utf-8
import time
import threading

from videos import urlconvert


class Load(threading.Thread):

    def __init__(self, queue, num):
        threading.Thread.__init__(self)
        self.queue = queue
        self.num = num

    def run(self):

        while self.queue.qsize() > 0:

            # 取得 queue 的資料
            url = self.queue.get()
            file_path = './'
            file_name = str(int(time.time() * 1000.0))

            # 處理資料
            print ("開始下載:" + str(self.num))
            urlconvert.mp4.store(url, file_path, file_name)
            print("下載結束")

            time.sleep(1)