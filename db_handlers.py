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


def add_message(user_id: int, text: str, date_query):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''INSERT INTO user_query(user_id, text, date_query) VALUES (%s, %s, %s)'''
    val = (user_id, text, date_query)
    cursor.execute(sql, val)
    conn.commit()
    conn.close()


def add_notification(user_id: int, notification_text: str, date_query):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''
        INSERT INTO user_notifications (user_id, notification_text, date_query)
        SELECT * FROM (SELECT '''+str(user_id)+''', "'''+notification_text+'''", "'''+str(date_query)+'''") AS tmp
        WHERE NOT EXISTS (
            SELECT user_id, notification_text  FROM user_notifications
            WHERE user_id='''+str(user_id)+''' AND notification_text = "'''+notification_text+'''"
        ) LIMIT 1;
    '''

    print(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()


def del_notification(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''DELETE FROM `user_notifications` WHERE user_id =''' + str(user_id)
    cursor.execute(sql)
    conn.commit()
    conn.close()


def get_notifications_list():
    conn = get_connection()
    cursor = conn.cursor()
    sql = '''SELECT * from `user_notifications`'''
    cursor.execute(sql)
    myresult = cursor.fetchall()
    # conn.commit()
    conn.close()
    return myresult
