import sqlite3
from datetime import datetime

DB_FILE = "terminal_market_data.db"

def get_db_connection():
    """Establishes an active connection to the SQLite database file."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    """Creates the structural tables required to store real-time data records."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS article_sentiment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT NOT NULL,
            headline TEXT NOT NULL,
            source TEXT NOT NULL,
            sentiment_score REAL NOT NULL,
            justification TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()
    print("🎯 Institutional SQLite database engine initialized successfully.")

if __name__ == "__main__":
    initialize_database()

