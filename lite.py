import sqlite3


class Database(object):
    # Initialize object with the file path 
    def __init__(self, db_name):
        self.db_name = db_name

    # Create a database connection and a cursor
    def connect_db(self):
        self.cnx = sqlite3.connect(self.db_name)
        self.cursor = self.cnx.cursor()
        
    # Create tables if they don't exist
    def create_db(self):
        self.connect_db()

        # Create scenarios table
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS scenarios 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT UNIQUE, scenario TEXT,
            o1 TEXT, o2 TEXT, o3 TEXT, o4 TEXT, o5 TEXT,
            i1 TEXT, i2 TEXT, i3 TEXT, i4 TEXT, i5 TEXT)
            """
        )

        # Create qaw table (qaw -> questions/answers/weights)
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS qaw (scenario INTEGER, question TEXT, answer TEXT, weight INTEGER,
            FOREIGN KEY (scenario) REFERENCES scenarios(id))
            """
        )

        self.cnx.commit()
        self.cnx.close()

    # Query the database
    def query_db(self, query, var):
        self.connect_db()
        self.cursor.execute(query, var)

        # If query is SELECT
        if query[0:6].lower() == 'select':  
            result = self.cursor.fetchall()
            self.cnx.close()
            return result
        else:
            self.cnx.commit()
            self.cnx.close()