from easySqlite3 import Db
from config import *
import unittest

class TestMethods(unittest.TestCase):
    def test_connect(self):
        db = Db(DATA_PATH)  # creata a data base object
        self.assertTrue(db.connect()) # connect to the data base
        db.close() # closing connection

    def test_close(self):
        db = Db(DATA_PATH)  # creata a data base object
        db.connect() # connect to the data base
        self.assertTrue(db.close()) # closing connection

    def test_prepareQuery(self):
        db = Db(DATA_PATH)  # creata a data base object
        db.connect() # connect to the data base
        self.assertTrue(INSERT_QUERY)  # prepare query
        db.close() # closing connection

    def test_createTable(self):
        db = Db(DATA_PATH)  # creata a data base object
        db.connect() # connect to the data base
        self.assertTrue(db.createTable(TABLE)) # create the table
        db.close() # closing connection

    def test_insertRow(self):
        db = Db(DATA_PATH)  # creata a data base object
        db.connect()  # connect to the data base
        db.prepareQuery(INSERT_QUERY)  # prepare query
        self.assertTrue(db.insertRow([999, "Fares", "Herhar"]))  # insert into table
        db.close()  # closing connection

    def test_justQuery(self):
        db = Db(DATA_PATH)  # creata a data base object
        db.connect()  # connect to the data base
        db.prepareQuery(JUST_QUERY)  # prepare query
        self.assertTrue(db.justQuery()) # the none result return query type
        db.close()  # closing connection

    def test_justQuery_1(self):
        db = Db(DATA_PATH)  # creata a data base object
        db.connect()  # connect to the data base
        db.prepareQuery(JUST_QUERY_1)  # prepare query
        self.assertTrue(db.justQuery(['New', 'Ilyes'])) # the none result return query type
        db.close()  # closing connection

    def test_extractData(self):
        db = Db(CHINOOK_PATH)  # creata a data base object
        db.connect()  # connect to the data base
        db.prepareQuery(DATA_QUERY)  # prepare query
        self.assertEqual(tuple(db.extractData()), ((1, 'Music'),)) # getting data from it
        db.close()  # closing connection

    def test_notTableOutPutQuey(self):
        db = Db(CHINOOK_PATH)  # creata a data base object
        db.connect()  # connect to the data base
        db.prepareQuery(COUNT_QUERY)  # prepare query
        self.assertEqual(db.notTableOutPutQuey(), 347) # like the count functions...
        db.close()  # closing connection
if __name__ == '__main__':
    unittest.main()