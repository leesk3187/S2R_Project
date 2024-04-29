from flask import *
from db import *
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.secret_key = 'test'
print(load_dotenv())
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userid = request.form.get('userid')
        userpw = request.form.get('userpw')

        user_info = (userid, userpw)
        result = sql_select(select_query, user_info)

        if result:
            flash("로그인 성공")
            return redirect(url_for('index'))
        else:
            flash("로그인 실패")
            return redirect(url_for('login'))
    else:
        return render_template("login.html")
    

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        userid = request.form.get('userid')
        userpw = request.form.get('userpw')
        email = request.form.get('email')
        username = request.form.get('username')
        userpwConfirm = request.form.get('userpwConfirm')


        insert_query = "INSERT INTO users (userID, PW, Email, name) VALUES (%s, %s, %s, %s)"
        user_info = (userid, userpw, email, username)
        if(userpw==userpwConfirm):
            if sql_insert(insert_query, user_info):
                flash("가입 성공!")
                return redirect(url_for('login'))
            else:
                flash("가입 실패")
                return redirect(url_for('register'))
        else:
            flash("비밀 번호를 확인하세요")
            return redirect(url_for('register'))

    return render_template("register.html")

@app.route('/password')
def password():
    return render_template("password.html")

@app.route('/map')
def map():
    google_maps_api_key= os.getenv("GOOGLE_API_KEY")
    return render_template("layout-static.html", google_maps_api_key=google_maps_api_key)

@app.route('/get_locations')
def get_locations_():
    locations = get_locations()
    print(locations)
    return jsonify(locations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=9999)