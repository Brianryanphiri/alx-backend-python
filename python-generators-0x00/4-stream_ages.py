import sqlite3

DB_FILE = "ALX_prodev.sqlite3"

def stream_user_ages():
    """Generator to yield user ages one by one."""
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield row[0]  # age is the first (and only) column
    cursor.close()
    connection.close()

def average_age():
    """Calculates and prints the average age using the generator."""
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1

    if count > 0:
        print(f"Average age of users: {total_age / count:.2f}")
    else:
        print("No users found.")

# Run it if the script is called directly
if __name__ == "__main__":
    average_age()
