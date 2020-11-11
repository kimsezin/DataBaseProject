from flask import Flask

app = Flask(__name__)

@app.route('/') #경로 지정 : '/'는 웹사이트 주소중 가장 상위
@app.route('/index') # '/', '/index 를 쳐도 똑같음
def hello():
    return 'Hello Web Framework World!!'

if __name__=='__main__':
    app.debug = True #디버그 모드로 작동 (코드를 수정할 시 자동으로 수정된 코드를 수행하는데 그것을 막아줌)
    app.run(host='127.0.0.1', port=5000) #어떤 어드레스의 포트로 돌릴건지 결정


