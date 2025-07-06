import sqlite3

DB_FILE = "ALX_prodev.sqlite3"

def stream_users():
    """Generator that yields one user row as a dict from the user_data table"""
    connection = sqlite3.connect(DB_FILE)
    connection.row_factory = sqlite3.Row  # To get dict-like rows
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM user_data")

    for row in cursor:
        yield dict(row)

    cursor.close()
    connection.close()
