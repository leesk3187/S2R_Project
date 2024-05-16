from flask import *
from db import *
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.secret_key = "test"

users = {
    'userid' : ''
}


@app.route("/")
def index():
    
    return render_template("index.html", title="S2R-Home")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        userid = request.form.get("userid")
        userpw = request.form.get("userpw")

        user_info = (userid, userpw)
        result = sql_select(select_query, user_info)

        if result:
            users['userid'] = userid
            session['userid'] = userid
            flash("로그인 성공")
            return redirect(url_for("index"))
        else:
            flash("로그인 실패")
            
            return redirect(url_for("login"))
    else:
        return render_template("users/login.html")
    
@app.route("/logout")
def logout():
    session.pop('userid', None)
    flash("로그아웃 되었습니다.")
    return redirect(url_for('index'))
    


@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        userid = request.form.get('userid')
        userpw = request.form.get('userpw')
        db_ip = request.form.get('db_ip')
        db_port = request.form.get('db_port')
        db_username = request.form.get('db_username')
        db_userpw = request.form.get('db_userpw')
        db_name = request.form.get('db_name')

        insert_query = "INSERT INTO users (userid, userpw, db_ip, db_port, db_username, db_userpw, db_name) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        user_info = (userid, userpw, db_ip, db_port, db_username, db_userpw, db_name)

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
    if 'userid' in session and session['userid'] == users['userid']:
        google_maps_api_key = os.getenv("GOOGLE_MAPS_API_KEY")
        return render_template(
            "layout-static.html", google_maps_api_key=google_maps_api_key, title="S2R-Map"
        )
    else:
        flash("로그인이 필요합니다.")
        return redirect(url_for('login'))


@app.route("/ip-list")  # IP List 페이지
def ip_list():
    if 'userid' in session and session['userid'] == users['userid']:
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
    if 'userid' in session and session['userid'] == users['userid']:
        return render_template(
            "tables.html"
        )
    else:
        flash("로그인이 필요합니다.")
        return redirect(url_for('login'))


@app.route("/success-ip")
def success_ip():
    if 'userid' in session and session['userid'] == users['userid']:
        return render_template(
            "success-ip.html", title="S2R-Success-IP"
        )
    else:
        flash("로그인이 필요합니다.")
        return redirect(url_for('login'))
    
@app.route("/failed-ip")
def failed_ip():
    if 'userid' in session and session['userid'] == users['userid']:
        return render_template(
            "failed-ip.html", title="S2R-Failed-IP"
        )
    else:
        flash("로그인이 필요합니다.")
        return redirect(url_for('login'))
    
    

@app.route("/get_locations")
def get_locations_():
    if 'userid' in session and session['userid'] == users['userid']:
        locations = get_locations()
        print(locations)
        return jsonify(locations)
    else:
        flash("로그인이 필요합니다.")
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=9999)
