import sqlite3

DB_PATH = 'db/database.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def execute_query(query, params=()):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor.lastrowid

def fetch_all(query, params=()):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

def fetch_one(query, params=()):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()
