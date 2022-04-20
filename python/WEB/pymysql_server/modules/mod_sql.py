#sql모듈 생성
#1.Class 생성 Database
#2.Class 생성이 될 때 ,pymysql.connect 변수 생성, cursor 생성 ->(__init__)함수에다가 생성
#3.init 제외 함수 3개 생성
#4.execute() 함수 만들 것 ->sql이랑 value 받아와서 sql문 실행
#5.executeALL() -> sql,value 받아와서 sql문 실행하고 결과값을 return
#6.commit()->commit을 하는 함수 만들기
#7.execute().executeAll()함수에서 value값은 디폴트 {}값 지정
#8.test를 해야되겠죠?? main.py모듈을 load 해서 가존에 sql작업을 모듈을 사용해서 코드를 작성

import pymysql


class Database():
    def __init__(self):
        self._db=pymysql.connect(host='localhost',
                                user="root",
                                password="aprl8752^^",
                                db ="ubion")
        self.cursor = self._db.cursor(pymysql.cursors.DictCursor)

    def execute(self,_sql,_values={}):
        self.cursor.execute(_sql,_values)

    def executeAll(self,_sql,_values={}):
        self.cursor.execute(_sql,_values)
        self.result=self.cursor.fetchall()
        return self.result
    def commit(self):
        self._db.commit()
