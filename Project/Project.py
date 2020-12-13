import sqlite3
from flask import Flask, render_template, request


 
app = Flask(__name__)
 

@app.route("/")
@app.route("/home")
def home():
   
    return render_template('home.html')

@app.route("/Client", methods=['GET','POST'])
def Client():
    db = sqlite3.connect('/home/kimsezin/DatabaseProject/Project/PetShop.db')
    db.row_factory = sqlite3.Row
    if request.method == 'POST':
        db.execute(
            'Insert into Client values(?,?,?,?,?);',
            (request.form['Phone Number'],request.form['Experience'],
            request.form['Have Many'], request.form['Age'],
            request.form['Location'])
        )
        db.commit()

        db.close()
        return render_template('Pet.html')
    else:

        return render_template('Client.html')

@app.route("/Center", methods=['GET','POST'])
def Center():
    db = sqlite3.connect('/home/kimsezin/DatabaseProject/Project/PetShop.db')
    db.row_factory = sqlite3.Row
    if request.method == 'POST':
        db.execute(
            'Insert into Center values(?,?,?,?,?);',
            (request.form['Center_Number'],request.form['Location'],
            request.form['Many_Pet'], request.form['Grade'],
            request.form['Pet_Hospital'])
        )
        db.commit()     

        db.close() 
        return render_template('OK.html')
    else :
        LastNumber_item = db.execute(
            'select Center_Number '
            ' from (select Center_Number from Center order by Center_Number desc limit 1)'
            ' order by Center_Number asc'
        ).fetchone()
    
        LastNumber = ord(LastNumber_item['Center_Number'])-47  
        
        db.close()

        return render_template('Center.html', LastNumber=LastNumber)
 
@app.route("/OK")
def OK():
    return render_template('OK.html')

@app.route("/Pet")
def Pet():
    # db = sqlite3.connect('/home/kimsezin/DatabaseProject/Project/PetShop.db')
    # db.row_factory = sqlite3.Row

    # items = db.execute(
    #     'select *'
    #     ' from Pet'
    # )

    # Pet_List = ""
    # for item in items :
    #     Pet_List += item[Pet_Number]
        
    return render_template('Pet.html')
if __name__ == "__main__":
    app.debug=True
    app.run(host='127.0.0.1',port=5001)
    