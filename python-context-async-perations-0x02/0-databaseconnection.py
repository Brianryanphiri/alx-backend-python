#!/usr/bin/env python3
import sqlite3

class DatabaseConnection:
    def __init__(self, db_name='users.db'):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn  # Return the connection to be used inside the with-block

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()
        # Returning False means any exception is propagated
        return False

# Usage of the context manager
with DatabaseConnection() as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print(results)
