import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    conn.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY)")
    conn.commit()
    conn.close()

def add_user(user_id):
    with sqlite3.connect("users.db") as conn:
        conn.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))

def get_all_users():
    with sqlite3.connect("users.db") as conn:
        return [row[0] for row in conn.execute("SELECT user_id FROM users")]
