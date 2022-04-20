from flask import Flask, render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')#html파일을 심어 렌더링한다


#@app.route('/corona')
#def corona():
#    corona_df = pd.read_csv('corona.csv') #데이터 프레임 형태
#    corona_df.columns=["인덱스","등록일시","사망자","확진자","게시글번호","기준일","기준시간","수정일시","누적의심자","누적확진률"]
#    return corona_df.to_html()

@app.route('/corona_des')
def corona_des():
    corona_df = pd.read_csv('corona.csv')
    corona_df.columns=["인덱스","등록일시","사망자","확진자","게시글번호","기준일","기준시간","수정일시","누적의심자","누적확진률"]
    corona_des=corona_df.describe()
    return corona_des.to_html()
    
@app.route('/corona')#지정하고싶은 함수명
def corona():
    corona_df = pd.read_csv('corona.csv')
    corona_df.columns=["인덱스","등록일시","사망자","확진자","게시글번호","기준일","기준시간","수정일시","누적의심자","누적확진률"]
    corona_df.sort_values("등록일시",inplace=True)
    corona_df["일일확진자"]=(corona_df['확진자']-corona_df['확진자'].shift()).fillna(0)
    corona_df["일일사망자"]=(corona_df['사망자']-corona_df['사망자'].shift()).fillna(0)
    corona_df.drop(["인덱스",'기준일','기준시간','수정일시','게시글번호'],axis=1,inplace=True)
    corona_df.reset_index(drop=True,inplace=True)
    corona_dict=corona_df.head(50).to_dict()
    cnt = len(corona_dict["등록일시"].keys())# No갯수 값을 줄이려면 len값을 줄여야함
    return render_template('corona.html', result=corona_dict, cnt=cnt)
    #result란이름으로 corona_dict를 쓰겠다 ! 어떤 이름으로 보낼지
    #corona.html파일 만들어주기     #corona.html을 파일에서 result를 뽑으면 corona _dict를 쓸수 있음

#판다스에서 그린 그래프 띄우기
@app.route("/img")
def img():
    corona_df = pd.read_csv('corona.csv')#지역변수여서 위의 값 못가져옴 csv파일 불러와서 꼭 지정해줘야함
    corona_df.columns=["인덱스","등록일시","사망자","확진자","게시글번호","기준일","기준시간","수정일시","누적의심자","누적확진률"]
    corona_df.sort_values("등록일시",inplace=True)#등록일시 기준으로 정렬해줌
    corona_df["일일 사망자"]=(corona_df['사망자']-corona_df['사망자'].shift()).fillna(0)#사망자만 그래프그릴것
    decide_cnt=corona_df.head(10)["일일 사망자"].values.tolist()#value에 뭘 넣어야하는지? 리스트형태 x축값 ,y축값 변수 만들어주기
    state_dt=corona_df.head(10)["등록일시"].values.tolist()
    plt.plot(state_dt,decide_cnt)
    img_1=BytesIO()#두개가 다 띄어진 채로 나오게 됨
    plt.savefig(img_1, format='png', dpi=200)
    img_1.seek(0)
    return send_file(img_1,mimetype='image/png')


app.run