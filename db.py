# db.py
import pymysql

def get_db_connection():
    conn = pymysql.connect(host='127.0.0.1', user='root', db='s2r', charset='utf8')
    return conn

def test_db_connection():
    conn = pymysql.connect(host='localhost', user='s2r',password='s2r', db='s2r', charset='utf8')
    return conn

def get_all_coordinates():
    try:
        conn = test_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT latitude, longitude FROM coordinates_table")  # 좌표 정보를 가져올 테이블 이름으로 수정
        coordinates = cur.fetchall()
        cur.close()
        conn.close()
        return coordinates
    except pymysql.MySQLError as e:
        print(f"SQL Error: {e}")
        return []

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

def get_all_ips(): # ip 가져오기
    try:
        conn = test_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT ip_address FROM ip_table")  # ip주소 컬럼 이름, ip테이블 이름 수정
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    except pymysql.MySQLError as e:
        print(f"SQL Error: {e}")
        return []



insert_query = "insert into register (userid, userpw) values(%s, %s)"
select_query = "select userid, userpw from register where userid=%s and userpw=%s"