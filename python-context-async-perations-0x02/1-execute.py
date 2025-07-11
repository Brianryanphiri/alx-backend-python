#!/usr/bin/env python3
import sqlite3

class ExecuteQuery:
    def __init__(self, query, params=None, db_name='users.db'):
        self.query = query
        self.params = params if params is not None else ()
        self.db_name = db_name
        self.conn = None
        self.results = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        cursor = self.conn.cursor()
        cursor.execute(self.query, self.params)
        self.results = cursor.fetchall()
        return self.results  # Return the query results

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()
        # Propagate exceptions if any
        return False

# Usage example
with ExecuteQuery("SELECT * FROM users WHERE age > ?", (25,)) as results:
    print(results)
