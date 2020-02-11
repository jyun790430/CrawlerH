# coding=utf-8

#https://www.runoob.com/python3/python-mysql-connector.html

import pymysql

class db:

    @staticmethod
    def cursor():
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='root',
            db='crawlh',
            charset='utf8'
        )

        return conn.cursor()
