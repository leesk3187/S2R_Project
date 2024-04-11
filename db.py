# db.py
import pymysql

def get_db_connection():
    conn = pymysql.connect(host='127.0.0.1', user='root', db='s2r', charset='utf8')
    return conn

def sql_select(query, data):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(query, data)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    except pymysql.MySQLError as e:
        print(f"SQL Error: {e}")
        return False

def sql_insert(query, data):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(query, data)
        conn.commit()
        cur.close()
        conn.close()
        return True
    except pymysql.MySQLError as e:
        print(f"SQL Error: {e}")
        return False

insert_query = "insert into register (userid, userpw) values(%s, %s)"
select_query = "select userid, userpw from register where userid=%s and userpw=%s"