from easySqlite3 import Db
from config import *

# for select from tables
db = Db(CHINOOK_PATH)  # creata a data base object
print(db.connect())  # connect to the data base
print(db.prepareQuery(DATA_QUERY))  # prepare query
for elem in db.extractData():
    print(elem)
print(db.close())  # closing connection


# for like the count functions
db = Db(CHINOOK_PATH)  # creata a data base object
print(db.connect())  # connect to the data base
print(db.prepareQuery(COUNT_QUERY))  # prepare query
print(db.notTableOutPutQuey())
print(db.close())  # closing connection