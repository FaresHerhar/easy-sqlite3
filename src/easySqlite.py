import sqlite3
from sqlite3 import Error


## https://www.guru99.com/sql-commands-dbms-query.html
class Db(object):
    """
    This module is used for managing Sqlite database.
    True, if the method works with success, False else.


    Data Definition Language (DDL): Create, Drop, ALter, Turncate
    Data Manipulation Language (DML): Grant, Revoke
    Data Control Language(DCL): Insert, Update, Delete
    Transaction Control Language(TCL): Commit, Rollback, Savepoint
    Data Query Language (DQL): Select
    """
    def __init__(self, db_name):
        self.__db_name = db_name
        self.__query = ''
        self.__conn = None
        self.__cur = None

    def connect(self):
        """Start COnnection to database."""
        try:
            self.__conn = sqlite3.Connection(self.__db_name)
            self.__cur = self.__conn.cursor()
            return True
        except Error:
            self.__conn.close()
            return False

    def close(self):
        """"Close a database."""
        try:
            self.__cur.close()
            self.__conn.close()
            return True
        except Error:
            return False

    def prepare_query(self, query):
        """
        This method can be called as many as you need.
        Before using any of the methods listed under, you should use this one before.
        
        Just to prepare the query, then call the second method like insertdata.
        quey = 'INSERT INTO tasks(data1, data2, data3...) VALUES(?,?,?...);'
        """
        try:
            self.__query = query
            return True
        except Error:
            return False

    def ddl_query(self, table_query):
        """This method is for Data Definition Language (DDL)."""
        try:
            self.__cur.execute(table_query)
            self.__conn.commit()
            return True
        except Error:
            return False

    def dcl_query(self, data=None):
        """This method is for Data Control Language (DML)."""
        try:
            if data is None:
                self.__cur.execute(self.__query)
            else:
                self.__cur.execute(self.__query, data)
            self.__conn.commit()
            return True
        except Error:
            return False

    def dql_query(self, data=None):
        """This method is for Data Query Language (DQL)."""
        try:
            if data is None:
                self.__cur.execute(self.__query)
            else:
                self.__cur.execute(self.__query, data)

            for row in self.__cur.fetchall():
                yield row
        except Error:
            yield None

    def count_quey(self, data=None):
        """This method is for when using count() function."""
        try:
            if data is None:
                self.__cur.execute(self.__query)
            else:
                self.__cur.execute(self.__query, data)

            d = self.__cur.fetchall()[0]
            return d[0]

        except Error:
            return None
