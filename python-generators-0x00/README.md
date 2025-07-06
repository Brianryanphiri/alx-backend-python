# Python Generators - ALX Backend Project

This project demonstrates how to use Python generators in the context of database operations. It sets up a simple SQLite database, inserts data from a CSV file, and streams rows one by one using a generator for memory-efficient data processing.

## Features

- Connects to an SQLite database (`ALX_prodev.sqlite3`).
- Creates a `user_data` table with fields: `user_id`, `name`, `email`, `age`.
- Loads sample user data from `user_data.csv`.
- Uses a Python generator to stream rows from the database one at a time.
- Includes example script `0-main.py` to run the full process.

## Getting Started

### Prerequisites

- Python 3.x installed (SQLite support is built-in).
- No additional database setup required.

### How to Run

1. Clone this repository.
2. Ensure `user_data.csv`, `seed.py`, and `0-main.py` are in the same directory.
3. Run the main script:

```bash
python 0-main.py
