# coding=utf-8

#https://www.runoob.com/python3/python-mysql-connector.html

import pymysql
from setting.config import MYSQL_CONN

class db:

    @staticmethod
    def conn():
        conn = pymysql.connect(
            host=MYSQL_CONN['host'],
            port=MYSQL_CONN['port'],
            user=MYSQL_CONN['user'],
            passwd=MYSQL_CONN['passwd'],
            db=MYSQL_CONN['db'],
            charset='utf8'
        )

        return conn
