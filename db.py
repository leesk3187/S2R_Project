# db.py
import pymysql

def get_db_connection():
    conn = pymysql.connect(host='localhost', user='root',password='0000', db='ips', charset='utf8')
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
    
# 위치 정보를 조회하는 쿼리 
def get_locations():
    select_query = "SELECT hostname, latitude, longitude FROM ipinfo"
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor() 
        cur.execute(select_query)

         # Decimal 타입을 float로 변환
        result = [(hostname, float(latitude), float(longitude)) for hostname, latitude, longitude in cur.fetchall()]
        return result
    except pymysql.MySQLError as e:
        print(f"SQL Error: {e}")
        return []
    finally:
        if conn:
            conn.close()

insert_query = "insert into register (userid, userpw) values(%s, %s)"
select_query = "select userid, userpw from register where userid=%s and userpw=%s"