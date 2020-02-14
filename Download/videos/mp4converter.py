# coding=utf-8

import os
import requests


class mp4:

    @staticmethod
    def store(url, file_path, file_name):

        file_name += '.mp4'
        _file = os.path.join(file_path, file_name)

        try:
            response = requests.get(url, stream=True)
            handle = open(_file, 'wb')
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    handle.write(chunk)

            return True

        except Exception as e:

            if os.path.isfile(_file):
                os.remove(_file)
                
            print file_name, str(e)

            return False