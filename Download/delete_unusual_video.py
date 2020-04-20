# coding=utf-8

import os

from model import CrawlVideoModel
from setting.config import VIDEO_FILE_PATH

data = CrawlVideoModel.Objects.getUnusualVideoName(1)

for k, row in enumerate(data):
    filename = row[0]
    filename += '.mp4'
    filepath = VIDEO_FILE_PATH

    _file = os.path.join(filepath, filename)

    if os.path.isfile(_file):
        print 'exists'
        #os.remove(_file)
    else:
        pass
