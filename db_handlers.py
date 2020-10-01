import sqlite3


def get_connection():
    connection = sqlite3.connect('user.db')
    return connection


def init_db(force: bool = False):
    conn = get_connection()
    cursor = conn.cursor()

    if force:
        cursor.execute('DROP TABLE IF EXISTS user_message')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_message(
        id          INTEGER PRIMARY_KEY,
        user_id     INTEGER NOT NULL,
        text        TEXT NOT NULL
        )
    ''')

    conn.commit()


def add_message(user_id: int, text: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_message (user_id,text) VALUES(?, ?)", (user_id, text))
    conn.commit()
