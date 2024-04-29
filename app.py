from flask import *
from db import *

from dotenv import load_dotenv # .env 파일 불러오기
import os # os 명령어 사용

app = Flask(__name__)
app.secret_key = 'test'

 # .env 파일 불러오기



@app.route('/')
def index():
    return render_template("index.html", title="HOME")

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

        user_info = (userid, userpw)
        result = sql_insert(insert_query, user_info)

        if result == True:
            flash("회원가입 성공!")
            return redirect(url_for('login'))
        else:
            flash("가입 실패")
            return redirect(url_for('register'))

    return render_template("register.html")

@app.route('/password')
def password():
    return render_template("password.html")

@app.route('/map')
def map():
    coordinates = get_all_coordinates()
    google_maps_api_key = os.getenv('GOOGLE_MAPS_API_KEY') # .env에서 해당 키 가져와서 변수에 저장. 변수를 통해 키에 접근 가능
    # 좌표 정보를 템플릿으로 전달하여 지도에 표시
    return render_template("layout-static.html", coordinates=coordinates, google_maps_api_key=google_maps_api_key)




@app.route('/ip-list') # IP List 페이지
def ip_list():
    ips = get_all_ips() # db.py에서 get_all_ips() 함수 가져옴 = ip 데이터
    return render_template("ip-list.html", ips=ips, title="IP LIST") # ip-list.html로 데이터 전달





if __name__ == '__main__':
    
    app.run(host='0.0.0.0', debug=True, port=9999)
    
    # 박