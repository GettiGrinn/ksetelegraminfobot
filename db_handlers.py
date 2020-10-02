import mysql.connector


def get_connection():
    connection = mysql.connector.connect(
          host="sql12.freemysqlhosting.net",
          user="sql12368189",
          password="C3pc4Wu3bJ",
          database="sql12368189",
          port="3306"
    )

    return connection


def init_db(force: bool = False):
    conn = get_connection()
    cursor = conn.cursor()

    if force:
        cursor.execute('DROP TABLE IF EXISTS user_query')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_query(
        id          INTEGER AUTO_INCREMENT PRIMARY KEY,
        user_id     INTEGER NOT NULL,
        text        VARCHAR(255) NOT NULL,
        date_query  DATETIME 
        )
    ''')

    conn.commit()


def add_message(user_id: int, text: str, date_query):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO user_query(user_id, text, date_query) VALUES (%s, %s, %s)'''
    val = (user_id, text, date_query)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()
