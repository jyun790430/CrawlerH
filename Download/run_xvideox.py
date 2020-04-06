# coding=utf-8

import Queue as queue
import threading

from videos import download
from setting.config import THREAD_NUM_XVIDEOX


website = 'xvideos'

_lock = threading.Lock()
_queue = queue.Queue()

threads = []
for i in range(THREAD_NUM_XVIDEOX):
  _t = download.Load(_queue, website, _lock)
  _t.start()
  threads.append(_t)