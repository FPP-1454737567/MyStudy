import pymysql


class DataBaseHandle(object):
    def __init__(self, host, user, password, port, dbname):
        conn = pymysql.connect(host=host,
                               user=user,
                               password=password,
                               port=port,
                               db=dbname)
        self.conn = conn

    def query_one_from_db(self, sql: str):
        cursor = self.conn.cursor()
        cursor.execute(sql)

        result = cursor.fetchone()
        return result

    def query_all_from_db(self, sql: str):
        cursor = self.conn.cursor()
        cursor.execute(sql)

        result = cursor.fetchall()
        return result

    def close_db(self):
        self.conn.close()
