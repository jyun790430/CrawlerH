# coding=utf-8

from model import conn
from setting.config import SERVER_ID

class Objects:

    @staticmethod
    def getUnDoneDetail(type, limit):
        _conn = conn.db.conn()
        cursor = _conn.cursor()
        cursor.execute("""
            SELECT
                id,
                origin_url,
                file_name 
            FROM
                crawl_video 
            WHERE
                TYPE = %s
                AND download =  0
                AND status = 0
            LIMIT %s
        """ % (type, limit))

        data = cursor.fetchall()
        _conn.close()
        return data

    @staticmethod
    def updateDetail(id, download, status, fileName=None):
        _conn = conn.db.conn()
        cursor = _conn.cursor()
        sql = """
             UPDATE crawl_video 
             SET download = %s,
                 status = %s,
                 server_id = %s
                 file_name
             WHERE
                 id = %s
        """ % (download, status, SERVER_ID, id)

        sql = sql.replace("file_name", ", file_name=\"" + fileName + "\"" if fileName else "")

        cursor.execute(sql)
        _conn.commit()
        _conn.close()


    @staticmethod
    def getVedioDetail(type, re_get):
        _conn = conn.db.conn()
        cursor = _conn.cursor()
        cursor.execute("""
                SELECT
                    id,
                    origin_url,
                    file_name 
                FROM
                    crawl_video 
                WHERE
                    TYPE = %s
                    AND re_get = %s
            """ % (type, re_get))

        data = cursor.fetchall()
        _conn.close()
        return data


    @staticmethod
    def reUpdateDetail(id, re_get, tags, categories):
        _conn = conn.db.conn()
        cursor = _conn.cursor()
        cursor.execute("""
                 UPDATE crawl_video 
                 SET re_get = %s , categories = "%s", tags = "%s"
                 WHERE
                     id = %s
            """ % (re_get, categories, tags,id))

        _conn.commit()
        _conn.close()


    @staticmethod
    def getUnusualVideoName(type):
        _conn = conn.db.conn()
        cursor = _conn.cursor()
        cursor.execute("""
            SELECT
                file_name 
            FROM
                crawl_video 
            WHERE
                type = %s
                AND status = 3
                AND download = 0
        """ % (type))

        data = cursor.fetchall()
        _conn.close()
        return data
