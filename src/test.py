import unittest

from easySqlite3 import Db
from config import *


class TestMethods(unittest.TestCase):
    def test_connect(self):
        db = Db(DATA_PATH)  # creata a data base object
        self.assertTrue(db.connect()) # connect to the data base
        db.close() # closing connection

    def test_close(self):
        db = Db(DATA_PATH)  # creata a data base object
        db.connect() # connect to the data base
        self.assertTrue(db.close()) # closing connection

    def test_prepare_query(self):
        db = Db(DATA_PATH)  # creata a data base object
        db.connect() # connect to the data base
        self.assertTrue(db.prepare_query(INSERT_QUERY))  # prepare query
        db.close() # closing connection

    def test_create_table(self):
        db = Db(DATA_PATH)  # creata a data base object
        db.connect() # connect to the data base
        self.assertTrue(db.create_table(TABLE)) # create the table
        db.close() # closing connection

    def test_insert_row(self):
        db = Db(DATA_PATH)  # creata a data base object
        db.connect()  # connect to the data base
        db.prepare_query(INSERT_QUERY)  # prepare query
        self.assertTrue(db.insert_row([1997, "Fares", "Herhar"]))  # insert into table
        db.close()  # closing connection

    def test_just_query(self):
        db = Db(DATA_PATH)  # creata a data base object
        db.connect()  # connect to the data base
        db.prepare_query(JUST_QUERY)  # prepare query
        self.assertTrue(db.just_query()) # the none result return query type
        db.close()  # closing connection

    def test_just_query_(self):
        db = Db(DATA_PATH)  # creata a data base object
        db.connect()  # connect to the data base
        db.prepare_query(JUST_QUERY_)  # prepare query
        self.assertTrue(db.just_query(['New', 'Ilyes'])) # the none result return query type
        db.close()  # closing connection

    def test_extractData(self):
        db = Db(CHINOOK_PATH)  # creata a data base object
        db.connect()  # connect to the data base
        db.prepare_query(DATA_QUERY)  # prepare query
        self.assertEqual(tuple(db.extract_data()), ((1, 'Music'),)) # getting data from it
        db.close()  # closing connection

    def test_notTableOutPutQuey(self):
        db = Db(CHINOOK_PATH)  # creata a data base object
        db.connect()  # connect to the data base
        db.prepare_query(COUNT_QUERY)  # prepare query
        self.assertEqual(db.not_table_out_put_quey(), 347) # like the count functions...
        db.close()  # closing connection


if __name__ == '__main__':
    unittest.main()