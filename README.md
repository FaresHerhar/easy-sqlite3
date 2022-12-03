# easySqlite3

## Description

A simple Python code for managing and working with the Sqlite3.

## Notes

***you can download the Sqlite data base browser [DB Browser for SQLite](https://sqlitebrowser.org/)***

> To start the connection to a data base.

`connect()`
  
> To close the connection linked to the current data base.

`close()`

## Sample

```python
from easySqlite3 import Db


TABLE = """\
CREATE TABLE IF NOT EXISTS profile(
  id INTEGER PRIMARY KEY,
  firstName TEXT NOT NULL,
  lastName TEXT NOT NULL
);
"""

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
db.create_table(TABLE)

# prepare query
db.prepare_query(INSERT_QUERY)

# insert into table
db.insert_row([999, 'Fares', 'Herhar'])

# closing connection
db.close()

# for select from tables
db = Db(CHINOOK_PATH)  # creata a data base object
print(db.connect())  # connect to the data base
print(db.prepare_query(DATA_QUERY))  # prepare query
for elem in db.extract_data():
    print(elem)
print(db.close())  # closing connection


# for like the count functions
db = Db(CHINOOK_PATH)  # creata a data base object
print(db.connect())  # connect to the data base
print(db.prepare_query(COUNT_QUERY))  # prepare query
print(db.not_table_out_put_query())
print(db.close())  # closing connection
```
