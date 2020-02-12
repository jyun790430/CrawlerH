# coding=utf-8


import Queue as queue
import threading

from videos import download



list = ['xvideos', 'pronhub']


for website in list:

    _lock = threading.Lock()
    _queue = queue.Queue()


    threads = []
    for i in range(5):
      _t = download.Load(_queue, website, _lock)
      _t.start()
      threads.append(_t)
