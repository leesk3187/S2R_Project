# db.py
import pymysql
import hashlib
import secrets
import random
import string

def get_db_connection():
    conn = pymysql.connect(host='localhost', user='root', password='0000', db='ips', charset='utf8')    
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
        print(f"SQL select Error: {e}")
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
        print(f"SQL insert Error: {e}")
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
def get_failed_ip(user_idx):
    try:
        select_query_db_info = "SELECT db_ip, db_port, db_username, db_userpw, db_name FROM users WHERE id_=%s" # 사용자 DB 정보 가져오기
        result = sql_select(select_query_db_info, (user_idx,))
        print(result[0])
        result = result[0]

        host, port, user, password, db = result
        port = int(port)
        password = '1234'

        conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset='utf8') # 사용자 DB 연결
        select_query = "SELECT * FROM ipInfo WHERE success=0"
        cur = conn.cursor() 
        cur.execute(select_query)
        result = cur.fetchall()
        print(result)
        return result
    except pymysql.MySQLError as e:
        print(f"SQL Error: {e}")
    
def get_success_ip(user_idx):
    try:
        select_query_db_info = "SELECT db_ip, db_port, db_username, db_userpw, db_name FROM users WHERE id_=%s" # 사용자 DB 정보 가져오기
        result = sql_select(select_query_db_info, (user_idx,))
        print(result[0])
        result = result[0]

        host, port, user, password, db = result
        port = int(port)
        password = '1234'

        conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset='utf8') # 사용자 DB 연결
        select_query = "SELECT * FROM ipInfo WHERE success=1"
        cur = conn.cursor() 
        cur.execute(select_query)
        result = cur.fetchall()
        print(result)
        return result
    
    except pymysql.MySQLError as e:
        print(f"SQL Error: {e}")


# id와 dbpw가 일치하는지 확인하는 쿼리
def check_userid_dbpw(user_id, db_userpw):
    check_query = "SELECT userid FROM users WHERE userid = %s AND db_userpw = %s"
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # user_id와 db_userpw 일치 여부 확인
        cursor.execute(check_query, (user_id, db_userpw))
        result = cursor.fetchone()
        if result:
            # ID와 PW가 일치함
            # 비밀번호 가져오기 함수 호출
            password = get_password_by_id(user_id)
            if password:
                # 비밀번호가 존재할 경우 임시 비밀번호 생성 함수 호출
                return reset_user_password(user_id)
            else:
                print("Password not found.")
                return None
        else:
            print("User ID and password do not match.")
            return None
    except pymysql.MySQLError as e:
        print(f"SQL Error: {e}")
        return None
    finally:
        if conn:
            conn.close()

# 임시 비밀번호 생성 함수
def reset_user_password(user_id):
    # 임시 비밀번호 생성
    temp_password = generate_temp_password()
    
    # 데이터베이스에서 사용자의 비밀번호 가져오기
    db_password = get_password_by_id(user_id)
    
    if db_password:
        # 새 비밀번호를 해싱하여 저장
        new_password = hash_password(temp_password)
        update_query = "UPDATE users SET userpw = %s WHERE userid = %s"
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(update_query, (new_password, user_id))
            conn.commit()
            return temp_password  # 생성된 임시 비밀번호 반환
        except pymysql.MySQLError as e:
            print(f"SQL Error: {e}")
            return None
        finally:
            if conn:
                conn.close()
    else:
        return None

# 사용자 ID를 기반으로 비밀번호를 가져오는 쿼리
def get_password_by_id(user_id):
    select_query = "SELECT userpw FROM users WHERE userid = %s"
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(select_query, (user_id,))
        password = cursor.fetchone()
        if password:
            return password[0]  # 해시된 비밀번호 반환
        else:
            return None
    except pymysql.MySQLError as e:
        print(f"SQL Error: {e}")
        return None
    finally:
        if conn:
            conn.close()

# 임시 비밀번호 생성 함수
def generate_temp_password():
    length = random.randint(8, 16)  # 8에서 16자리 사이의 길이 선택
    special_character = '@'
    all_characters = string.ascii_letters + string.digits + special_character
    while True:
        temp_password = ''.join(random.choice(all_characters) for _ in range(length))
        if (any(c.islower() for c in temp_password) and
            any(c.isupper() for c in temp_password) and
            any(c.isdigit() for c in temp_password) and
            special_character in temp_password):
            break
    return temp_password

# 비밀번호를 해싱하는 함수
def hash_password(password):
    # 비밀번호를 해싱하여 반환
    return hashlib.sha256(password.encode()).hexdigest()

insert_query = "insert into register (userid, userpw) values(%s, %s)"
select_query = "select userid, userpw from register where userid=%s and userpw=%s"