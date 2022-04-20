from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return"Hello, World"
#/대신 /second을 추가해서 def을 실행하려면 어떻게????
@app.route('/second/')#/를 넣고 짜고 주소창에서 넣거나 뺼 경우 오류안생김, /안넣고 짜면 주소창에서 안넣으면 오류
def second():#함수명 index랑 다르게해야함 
    return"second page"# 주소창에 ~/second/치면 나옴 
app.run
#플라스크 실행시 cd C:\Users\heeyeon\Desktop\2022\빅데이터 분석\WEB\server 경로설정하고
#set FLASK_APP=main(파일이름
#flask run하면  http://127.0.0.1:5000/  url 채팅창에 입력 http://127.0.0.1:5000/second 채팅창에 입력
#flask 실행전에 cd 경로설정확인하고 set하기
