from flask import *
from db import *
from dotenv import load_dotenv
import os
import hashlib, re

app = Flask(__name__)
app.secret_key = "test"

@app.route("/")
def index():
    if 'uid' in session:
        print(1)
        
        return render_template("index.html", title="S2R-Home")
    else:

        return render_template("index.html", title="S2R-Home")
    

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        userid = request.form.get("userid")
        userpw = request.form.get("userpw")
        userpw = hashlib.sha256(userpw.encode()).hexdigest()

        user_info = (userid, userpw)
        select_query = "select * from users where userid=%s and userpw=%s"
        result = sql_select(select_query, user_info)

        if result[0][1] == userid and result[0][2] == userpw: # 입력한 비번과 DB 저장된 정보 비교
            session['uid'] = result[0][0] # 세션 관리 시작
            flash("로그인 성공")
            return redirect(url_for("index"))
        else:
            flash("로그인 실패")
            
            return redirect(url_for("login"))
    else:
        return render_template("users/login.html")
    
@app.route("/logout", methods=["POST"])
def logout():
    if request.method == 'POST':
        try:

            session.clear()

            flash("로그아웃 되었습니다.")
            return redirect(url_for('index'))
        except:
            flash("로그인 하세요")
            return redirect(url_for('index'))


@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':

        pattern = r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)(\.|$)){4}$'

        userid = request.form.get('userid')
        userpw = request.form.get('userpw')
        db_ip = request.form.get('db_ip')
        db_port = request.form.get('db_port')
        db_username = request.form.get('db_username')
        db_userpw = request.form.get('db_userpw')
        db_name = request.form.get('db_name')

        check_userid_query = "SELECT * FROM users WHERE userid=%s"
        existing_user = sql_select(check_userid_query, (userid,))

        userid_len = len(userid)
        userpw_len = len(userpw)

        if existing_user:
            if existing_user[0][1] == userid:
                flash("중복된 아이디입니다.")
                return redirect(url_for('register'))

        try:
            db_port = int(db_port)
        except ValueError:
            flash("DB 포트 번호가 유효하지 않습니다. 정수를 입력해 주세요.")
            return redirect(url_for('register'))
        
        if (userid_len >= 4 and userid_len <= 16) and (userpw_len >= 8 and userpw_len <= 16): # 아이디 비번 자릿수 검사
            if (db_port > 0 and db_port <= 65535 and re.match(pattern, db_ip)): # DB 포트 및 ip 검사
                userpw = hashlib.sha256(userpw.encode()).hexdigest()

                insert_query = "INSERT INTO users (userid, userpw, db_ip, db_port, db_username, db_userpw, db_name) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                user_info = (userid, userpw, db_ip, db_port, db_username, db_userpw, db_name)
                print("register test")
                if sql_insert(insert_query, user_info):
                    flash("가입 성공!")
                    return redirect(url_for('login'))
                else:
                    flash("가입 실패")
                    return redirect(url_for('register'))
    

    return render_template("users/register.html")


@app.route("/password")
def password():
    return render_template("users/password.html")


@app.route("/map")
def map():
    if 'uid' in session:
        google_maps_api_key = os.getenv("GOOGLE_MAPS_API_KEY")
        return render_template(
            "map.html", google_maps_api_key=google_maps_api_key, title="S2R-Map"
        )
    else:
        flash("로그인이 필요합니다.")
        return redirect(url_for('login'))


@app.route("/ip-list")  # IP List 페이지
def ip_list():
    if 'uid' in session:
        ips = get_all_ips()  # db.py에서 get_all_ips() 함수 가져옴 = ip 데이터
        print(ips)
        return render_template(
            "ip-list.html", ips=ips, title="S2R-IP List"
        )  # ip-list.html로 데이터 전달
    else:
        flash("로그인이 필요합니다.")
        return redirect(url_for('login'))


@app.route("/tables")
def tables():
    if 'uid' in session:
        return render_template(
            "tables.html"
        )
    else:
        flash("로그인이 필요합니다.")
        return redirect(url_for('login'))


@app.route("/success-ip")
def success_ip():
    if 'uid' in session:
        return render_template(
            "success-ip.html", title="S2R-Success-IP"
        )
    else:
        flash("로그인이 필요합니다.")
        return redirect(url_for('login'))
    
@app.route("/failed-ip")
def failed_ip():
    if 'uid' in session:
        return render_template(
            "failed-ip.html", title="S2R-Failed-IP"
        )
    else:
        flash("로그인이 필요합니다.")
        return redirect(url_for('login'))
    

@app.route("/get_locations")
def get_locations_():
    if 'uid' in session:
        locations = get_locations(session['uid'])
        return jsonify(locations)
    else:
        flash("로그인이 필요합니다.")
        return redirect(url_for("login"))
    
# 비밀번호 초기화 엔드포인트
@app.route('/check_userid_dbpw', methods=['POST'])
def reset_password():
    data = request.json
    user_id = data.get('userId')
    db_pw = data.get('dbPw')

    if not user_id or not db_pw:
        return jsonify({"message": "User ID and database password are required"}), 400

    reset_result = check_userid_dbpw(user_id, db_pw)  # db_pw 인자를 전달해야 합니다.
    if reset_result:
        return jsonify({"tempPassword": reset_result}), 200
    else:
        return jsonify({"message": "Failed to reset password"}), 400  # 실패 시 400번 상태 코드를 반환합니다.
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=9999)