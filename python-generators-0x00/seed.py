import sqlite3
import csv
import uuid
import os

DB_FILE = "ALX_prodev.sqlite3"

def connect_db():
    """Connects to SQLite database (creates file if not exists)"""
    return sqlite3.connect(DB_FILE)

def create_database(connection):
    """No-op for SQLite — database is created with the file"""
    pass  # SQLite auto-creates the DB file

def connect_to_prodev():
    """Just reconnect to the same SQLite file"""
    return sqlite3.connect(DB_FILE)

def create_table(connection):
    """Creates user_data table if it doesn't exist"""
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            age REAL NOT NULL
        )
    """)
    connection.commit()
    cursor.close()
    print("Table user_data created successfully")

def insert_data(connection, csv_file):
    """Inserts data from CSV into SQLite database"""
    if not os.path.exists(csv_file):
        print(f"❌ File '{csv_file}' not found.")
        return

    cursor = connection.cursor()
    with open(csv_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                uid = str(uuid.UUID(row['user_id']))  # validate UUID
            except ValueError:
                print(f"Invalid UUID: {row['user_id']}")
                continue

            # Check if the record already exists
            cursor.execute("SELECT user_id FROM user_data WHERE user_id = ?", (uid,))
            if not cursor.fetchone():
                cursor.execute("""
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (?, ?, ?, ?)
                """, (uid, row['name'], row['email'], float(row['age'])))
    connection.commit()
    cursor.close()
    print(f"Data from {csv_file} inserted successfully")
