import sqlite3
from config.tables.players import players

DATABASE = "players.db"

def connect_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def generate_tables():
    all_tables = [players]
    db = connect_db()
    cursor = db.cursor()

    for table in all_tables:
        for row in table:
            cursor.execute(row)