TABLE = """
        CREATE TABLE IF NOT EXISTS profile(
        id INTEGER PRIMARY KEY,
        firstName TEXT NOT NULL,
        lastName TEXT NOT NULL
        );
        """

CHINOOK_PATH = 'data/chinook.db'
DATA_PATH = 'data/data.db'

# the query for inserting into a table
INSERT_QUERY = 'INSERT INTO profile(id, firstName, lastName) VALUES (?, ?, ?)'

# two different senarios
JUST_QUERY = "UPDATE profile SET firstName=\"Ilyes\" WHERE lastName=\"Herhar\";"
JUST_QUERY_1 = "UPDATE profile SET firstName = ? WHERE lastName = ? ;"

# data exctract query
DATA_QUERY = "SELECT * FROM playlists LIMIT 1;"

# for count function
COUNT_QUERY = "SELECT COUNT(*) FROM albums;"
