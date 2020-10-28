from flask import Flask
from flask import render_template
import sqlite3

@app.route('restaurants/<int:restaurant_id>/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id)
    db=sqlite3.connect("restaurant_menu.db")
    db.row_factory=sqlite3.Row
    if request.method == 'POST' : #클라이언트에서 메소드를 호출하게 되면 그 정보를 갖고있는 전역변수
        db.excute(
            'UPDATE menu_item SET'
            ' name=?'
            ' WHERE id =?',
            (request.form['name'],menu_id)#키로 name을 사용
        )
        db.commit()
        db.close()
        return redirect(url_for('restaurantMenu',restaurant_id=restaurant_id))
    else:
        editedItem = db.execute(
            'SELECT *'
            ' FROM menu_item'
            ' WHERE id=?',
            (menu_id,)
        ).fetchone()
        db.close()
        return render_template(
            'editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem
        )