import sqlite3
import os

DB_PATH = 'db/database.db'
SQL_FILE = 'db/init_db.sql'

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    existing_tables = {table[0] for table in cursor.fetchall()}
    print(f"Existing tables: {existing_tables}")

    with open(SQL_FILE, 'r') as sql_file:
        sql_script = sql_file.read()

    cursor.executescript(sql_script)

    connection.commit()
    connection.close()
    print("✅ Database initialized or updated successfully!")

if __name__ == '__main__':
    init_db()