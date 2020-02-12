# coding=utf-8

import os
import requests

class mp4:

    @staticmethod
    def store(url, file_path, file_name):

        response = requests.get(url, stream=True)

        file_name += '.mp4'
        _file = os.path.join(file_path, file_name)

        handle = open(_file, 'wb')
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                handle.write(chunk)

        return True