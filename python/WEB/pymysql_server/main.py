
from flask import Flask, redirect, render_template, request, url_for
from modules import mod_sql

app = Flask(__name__)

#localhost로 접속했을 떄 빈url 그밑의 함수를 구동해서 보여주겠따.
@app.route("/")
def index():
    return render_template("index.html")# 어떤 url을렌더링 할지 

#포트번호 지정하기 ->만만한 포트번호 80 

#localhost/signup로 접속했을때
@app.route("/signup/",methods=["GET"])
def signup():
    return render_template("signup.html")
@app.route("/signup",methods=["POST"])
def signup_2():
    _id = request.form["_id"]  #post형식이라 form으로 받음
    _password = request.form["_password"]#키값은 name값을 가져옴
    _name = request.form["_name"]
    _phone = request.form["_phone"]
    _ads = request.form["_ads"]
    _regitdate = request.form["_regitdate"]
    _age = request.form["_age"]
    _gender = request.form["_gender"]
    sql = """
            INSERT INTO user_info VALUES (
                %s,%s,%s,%s,%s,%s,%s,%s)
        """
    _values = [_id,_password,_name,_phone,_ads,_gender,_age,_regitdate]# 컬럼순서대로
    _db=mod_sql.Database()
    _db.execute(sql,_values)
    _db.commit()
    return redirect(url_for('index')) #인덱스 함수명넣기->인덱스 화면으로 넘어감
    
@app.route("/login/",methods=["POST"])
def login():
    #db->select문을 사용해->index페이지에 있는 input ID PASSWORD 받아와서 SELECT문으로 조회
    #결과값 존재시 return 'login', 존재하지 않으면 'fail'
    _id = request.form["_id"]
    _password = request.form["_password"]
    #print(_id,_password) -2번완료
    sql = '''
                SELECT * FROM user_info WHERE ID =%s AND password=%s
         '''
    _values =[_id,_password]
    _db=mod_sql.Database()
    result=_db.executeAll(sql,_values)
    print(result)

    if result:
        return render_template("welcome.html", name=result[0]["name"],id=result[0]["ID"])#다른페이지 보여주기
    else:
        return redirect(url_for('index'))#다시 실행

@app.route("/update", methods=["GET"])
def update():
    id=request.args["_id"]
    sql='''SELECT * FROM user_info WHERE ID=%s
    '''
    values=[id]
    _db = mod_sql.Database()
    result =_db.executeAll(sql,values)
    return render_template("update.html",info = result[0])

@app.route("/update", methods=["POST"])
def update_2():
    _id = request.form["_id"]  #post형식이라 form으로 받음
    _password = request.form["_password"]#키값은 name값을 가져옴
    _name = request.form["_name"]
    _phone = request.form["_phone"]
    _ads = request.form["_ads"]
    _age = request.form["_age"]
    _gender = request.form["_gender"]
    sql="""update user_info set 
            password=%s,
            name=%s,
            phone=%s,
            gender=%s,
            age=%s,
            ads=%s
            WHERE ID=%s
        """
    values=[_password,_name,_phone,_gender,_age,_ads,_id]
    _db = mod_sql.Database()
    _db.execute(sql,values)
    _db.commit()
    return redirect(url_for('index'))
#회원탈퇴
@app. route("/delete",methods=["get"])
def delete():
    _id = request.args["_id"]
    return render_template("delete.html",id=_id)

@app.route("/delete",methods=["post"])
def delete_2():
    _id = request.form["_id"] 
    _password = request.form["_password"]
    _db = mod_sql.Database()
    s_sql = """
                SELECT * FROM user_info WHERE ID=%s AND password = %s
            """
    d_sql = """
                DELETE FROM user_info WHERE ID=%s AND password = %s
            """
    _values = [_id,_password]
    result = _db.executeAll(s_sql,_values)
    if result: #결과값이 존재하지 않으면 
        _db.execute(d_sql,_values)
        _db.commit()
        return redirect(url_for('index'))#함수명 부름
    else:
        return "패스워드가 일치하지 않습니다"
        
#데이터보기        
@app.route("/view", methods=["get"])
def _view():
    sql = """
            SELECT 
            user_info.name,
            user_info.ads,
            user_info.age,
            ads_info.register_count
            FROM 
            user_info 
            LEFT JOIN 
            ads_info 
            ON 
            user_info.ads=ads_info.ads
        """
    _db=mod_sql.Database()
    result =_db.executeAll(sql)
    key= list(result[0].keys())
    return render_template("view.html",result=result,keys=key)#키값은맘대로 여기 키값을 view.html 키값에 넣어줘여함

app.run(port=80, debug=True)  