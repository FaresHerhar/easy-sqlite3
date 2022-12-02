import sqlite3
from sqlite3 import Error


class Db(object):
    def __init__(self, db_name):
        self.__db_name = db_name
        self.__query = ''
        self.__conn = None
        self.__cur = None

    def connect(self):
        try:
            self.__conn = sqlite3.Connection(self.__db_name)
            self.__cur = self.__conn.cursor()
            return True
        except Error:
            self.__conn.close()
            return False

    def close(self):
        try:
            self.__cur.close()
            self.__conn.close()
            return True
        except Error:
            return False

    def create_table(self, table_query):
        try:
            self.__cur.execute(table_query)
            self.__conn.commit()
            return True
        except Error:
            return False

    def prepare_query(self, query):
        try:
            self.__query = query
            return True
        except Error:
            return False

    def insert_row(self, data):
        try:
            self.__cur.execute(self.__query, data)
            self.__conn.commit()
            return True
        except Error:
            return False

    def just_query(self, data=None):
        try:
            if data is None:
                self.__cur.execute(self.__query)
            else:
                self.__cur.execute(self.__query, data)
            self.__conn.commit()
            return True
        except Exception as e:
            return False

    def extract_data(self, data=None):
        try:
            if data is not None:
                self.__cur.execute(self.__query, data)
            else:
                self.__cur.execute(self.__query)

            for row in self.__cur.fetchall():
                yield row
        except Error:
            yield None

    def not_table_out_put_quey(self, data=None):
        try:
            if data is not None:
                self.__cur.execute(self.__query, data)
            else:
                self.__cur.execute(self.__query)

            d = self.__cur.fetchall()[0]
            return d[0]

        except Error:
            return None
