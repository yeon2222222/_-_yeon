from flask import Flask,render_template, request #render_template 꼭 붙이기,

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')#index.html파일을 불러옴, 하위 폴더templates에 index.html 파일 만들어 두기
#http://127.0.0.1:5000/로 열기
@app.route('/second/')#두번쨰 url 추가 항상 저장 !!
def second():#함수명은 반드시 다르게! 
    _id =request.args.get("id") #키값넣기
    _pass =request.args.get("pass")
    print(_id,_pass)#print값은 프롬프트 화면에 내가 적은 데이터가 나옴
    return render_template("second.html",id=_id,_pass=_pass)#html을 렌더링할떄 id라는 이름으로 세컨드페이지를 불러왔을떄 다시 html이랑 보내주겟다
    #if _id =="aaa" and _pass=="sss":
    #   return render_template("second.html")
    #else:
    #    return "로그인에 실패" #return ren~("")로 바꿔도됌

    # second.html파일 다시 하위 폴더에 만든 후 실행 
#url을 매번 칠수 없으니 하이퍼링크를 걸어야함 , index파일에서 a태그 이용해서 url바꿔주기
@app.route('/third/',methods=["POST"])
def third():#위에 _id랑 다름 :지역변수
    _id= request.form['id']#인덱스에서 지정한 name이 id
    _pass=request.form['pass']
    print(_id,_pass)
    return "HELLO"
app.run 
#http://127.0.0.1:5000/second/로 열기
#cmd에 set FLASK_APP=data flask run 해서 구동
