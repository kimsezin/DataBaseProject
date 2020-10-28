from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/restaurant/<int:restaurant_id>/')

def restaurant(restaurant_id):
    db = sqlite3.connect("restaurant_menu.db") #db 핸들 연결
    db.row_factory = sqlite3.Row #접근할 때 키로 접근하겠다.
    items = db.execute( 
        'SELECT name, id, price, description' #query하는것
        ' FROM menu_item'
        ' WHERE restaurant_id=?', (restaurant_id,)
    ).fetchall() #튜플이 여러개 있으니 다 읽어오라. 다읽어올땐 리스트로 저장
    output = '' #비어있는 문자열 
    for item in items:
        output += item['name'] + '<br>' #br은 줄 바꿈 
        output += item['price'] + '<br>'
        output += itemp['description'] + '<br>'
        #이름 줄바꿈 가격 줄바꿈 설명 줄바꿈

    db.close()
    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5001)