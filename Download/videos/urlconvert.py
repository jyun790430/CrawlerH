# coding=utf-8

import urllib3


class mp4:

    @staticmethod
    def store(url, file_path, file_name):
        #urllib3.disable_warnings()
        http = urllib3.PoolManager()
        resp = http.request('GET', url, preload_content=False)

        _file = file_path + file_name + '.mp4'

        with open(_file, 'wb') as out:
            while True:
                data = resp.read(1024)
                if not data:
                    break
                out.write(data)
        resp.release_conn()