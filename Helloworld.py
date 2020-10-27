from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello():
    return 'Hello Web Framework World!'

if __name__=='__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)