# coding=utf-8

import os
import subprocess

from model import conn
from setting.config import VIDEO_FILE_PATH

files = os.listdir(VIDEO_FILE_PATH)

for _f in files:
    fullpath = os.path.join(VIDEO_FILE_PATH, _f)
    result = subprocess.Popen(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', fullpath], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        #result = subprocess.Popen(['ffprobe', '-i', fullpath, '-v', 'quiet', '-show_entries', 'format=duration', '-of', 'csv', "p=0"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    out, err = result.communicate()

    print '========================================'
    _f = _f.replace(".mp4", "")
    _f = _f.replace(" ", "")
    _f = str(_f.strip())
    print out, _f

    _conn = conn.db.conn()
    cursor = _conn.cursor()

    if not out:
        continue

    sql = """
        update crawl_video set duration = %s where unique_token = "%s"
    """ % (out, _f)

    try:
        cursor.execute(sql)
        _conn.commit()
        _conn.close()
    except:
        pass
