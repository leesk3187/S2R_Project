# db.py
import pymysql

def get_db_connection():
    conn = pymysql.connect(host='localhost', user='root',password='0000', db='ips', charset='utf8')
    return conn


def ip_db_connection(): # ip-list db 따로 구성할 경우 수정
    conn = pymysql.connect(host='localhost', user='s2r',password='s2r', db='s2r', charset='utf8')
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
    
def get_all_ips(): # ip 가져오기
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT ip, hostname, latitude, longitude, city,region,country_name, access_,accessTIme  FROM ipinfo") 
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
    except pymysql.MySQLError as e:
        print(f"SQL Error: {e}")
        return []
    
    
    
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

# 사용자 ID를 기반으로 비밀번호를 가져오는 쿼리
def get_password_by_id(user_id):
    select_query = "SELECT userpw FROM users WHERE userid = %s"
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(select_query, (user_id,))
        password = cursor.fetchone()
        print(password)
        return password
    except pymysql.MySQLError as e:
        print(f"SQL Error: {e}")
        return None
    finally:
        if conn:
            conn.close()

# 사용자의 비밀번호를 초기화하는 함수
def reset_user_password(user_id):
    update_query = "UPDATE users SET userpw = %s WHERE userid = %s"
    new_password = "reset0513"
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(update_query, (new_password, user_id))
        conn.commit()
        return True
    except pymysql.MySQLError as e:
        print(f"SQL Error: {e}")
        return False
    finally:
        if conn:
            conn.close()
                     
insert_query = "insert into register (userid, userpw) values(%s, %s)"
select_query = "select userid, userpw from register where userid=%s and userpw=%s"