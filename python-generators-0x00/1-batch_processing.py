import sqlite3

DB_FILE = "ALX_prodev.sqlite3"

def stream_users_in_batches(batch_size):
    connection = sqlite3.connect(DB_FILE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    offset = 0
    while True:
        cursor.execute("SELECT * FROM user_data LIMIT ? OFFSET ?", (batch_size, offset))
        rows = cursor.fetchall()
        if not rows:
            break
        yield [dict(row) for row in rows]
        offset += batch_size

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                yield user
