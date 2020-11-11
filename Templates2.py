from flask import Flask
from flask import render_template
import sqlite3

app = Flask(__name__)

@app.route('/restaurant/<int:restaurant_id>')
def restaurantMenu(restaurant_id):
    db = sqlite3.connect("restaurant_menu.db")
    db.row_factory=sqlite3.Row

    restaurant = db.execute(
        'SELECT id, name'
        ' FROM restaurant'
        ' WHERE id=?', (restaurant_id,)
    ).fetchone()
    items = db.execute(
        'SELECT name, id, price, description'
        ' FROM menu_item'
        ' WHERE restaurant_id=?',(restaurant_id),
    ).fetchall()
    db.close()
    return render_template('menu.html', restaurant=restaurant, items=items)

if __name__ =='__main__':
    app.debug=True
    app.run(host='127.0.0.1', port=5004)