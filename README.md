DISCRIPTION:
------------
A very simple Library for managing and working with the Sqlite3 Library, 
under Python Language.

Please make it better.

THE HIRARCHY:
-------------
```
    easySqlite3
├── easySqlite3.py
├── __init__.py
└── README.md

```

TOOLS:
------
* Language
	* Python

*  Version
	* 3.5

* Libraries
	* re
	* sqlite3

NOTES:
------
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

```

AUTHOR:
-------
* HERHAR Fares
* DZ, Algeria
* herhar.fares@yandex.com