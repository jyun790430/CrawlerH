# coding=utf-8

from model import conn


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

        return cursor.fetchall()

    @staticmethod
    def updateDetail(id, download, status):
        _conn = conn.db.conn()
        cursor = _conn.cursor()
        cursor.execute("""
             UPDATE crawl_video 
             SET download = %s,
                 status = %s 
             WHERE
                 id = %s
        """ % (download, status, id))
        _conn.commit()


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

        return cursor.fetchall()


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
