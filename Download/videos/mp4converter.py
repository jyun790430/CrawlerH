# coding=utf-8

import os
import requests
import mimetypes

class mp4:

    @staticmethod
    def store(url, file_path, file_name):

        response = requests.get(url, stream=True)
        if response.status_code == 200:
            try:
                content_type = response.headers['content-type']
                extension = mimetypes.guess_extension(content_type)

                file_name += extension
                _file = os.path.join(file_path, file_name)

                handle = open(_file, 'wb')
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        handle.write(chunk)

                res = dict()
                res['fileName'] = file_name
                return res

            except Exception as e:

                if os.path.isfile(_file):
                    os.remove(_file)

                print file_name, str(e)
        else:
            print 'Http Status:' + str(response.status_code) + "Fail File" + file_name

        return False