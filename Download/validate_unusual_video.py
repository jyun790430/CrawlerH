# coding=utf-8

import os
import subprocess

from model import CrawlVideoModel
from setting.config import VIDEO_FILE_PATH

files = os.listdir(VIDEO_FILE_PATH)
a = subprocess.Popen(['ffmpeg', '-i', '/Users/bryson/videoH/46ca6786ceaf078653acf3e9b0cd13bb.mp4'])
print a.returncode

# # 以迴圈處理
# for _f in files:
#   # 產生檔案的絕對路徑
#   fullpath = os.path.join(VIDEO_FILE_PATH, _f)
#   # 判斷 fullpath 是檔案還是目錄
#   if os.path.isfile(fullpath):
#     print(fullpath)
#     result = subprocess.Popen(['ffmpeg', '-i', fullpath])
#     text = result.communicate()
#     print(result.returncode)
#     #break


#
# for k, row in enumerate(data):
#     filename = row[0]
#     filename += '.mp4'
#     filepath = VIDEO_FILE_PATH
#
#     _file = os.path.isfile(filepath, filename)
#
#     if os.path.isfile(_file):
#         print 'exists'
#         #os.remove(_file)
#     else:
#         pass
