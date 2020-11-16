from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/home/')
def home():
    return render_template('main.html')

if __name__ =='__main__':
    app.debug=True
    app.run(host='127.0.0.1', port=5000)