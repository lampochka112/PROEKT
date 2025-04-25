import sqlite3

def init_db():
    conn = sqlite3.connect("bot.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            banned BOOLEAN DEFAULT FALSE
        )
    """)
    conn.commit()
    conn.close()

def add_user(user_id, username):
    conn = sqlite3.connect("bot.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users VALUES (?, ?, ?)", (user_id, username, False))
    conn.commit()
    conn.close() 