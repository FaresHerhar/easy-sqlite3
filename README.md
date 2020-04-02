DISCRIPTION:
------------
A very simple Library for managing and working with the Sqlite3 Library, 
under Python Language.

Please make it better.

THE HIRARCHY:
-------------
```
    easySqlite3
├── __init__.py
├── config.py
├── data
│   ├── chinook.db
│   └── data.db
├── easySqlite3.py
├── test.py
└── README.md
```

TOOLS:
------
* Language
	* Python 3.5

* Libraries
	* re
	* sqlite3
  * unittest

NOTES:
------
## you can download the Sqlite data base browser
# [DB Browser for SQLite](https://sqlitebrowser.org/)
### find tests for all the methodes, in the test.py, and __init__.py
* connect()
  >To start the connection to a data base.

* close()
  >To close the connection linked to the current data base.

SAMPLE:
-------
```
from easySqlite3 import Db


TABLE = \'''
        CREATE TABLE IF NOT EXISTS profile(
        id INTEGER PRIMARY KEY,
        firstName TEXT NOT NULL,
        lastName TEXT NOT NULL
        );
        \'''

DATA_BASE_PATH = 'db.sql'
INSERT_QUERY = 'INSERT INTO profile(id, firstName, lastName) VALUES (?, ?, ?)'

#------------------#
# the tests
#------------------#

# start an data base object
db = Db(DATA_BASE_PATH)

# connect to the data base
db.connect()

# create the table
db.createTable(TABLE)

# prepare query
db.prepareQuery(INSERT_QUERY)

# insert into table
db.insertRow([999, 'Fares', 'Herhar'])

# closing connection
db.close()

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

```