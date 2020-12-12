import sqlite3
from flask import Flask, render_template


 
app = Flask(__name__)
 

@app.route("/")
def home():
   
    return render_template('home.html')

@app.route("/Client")
def Client():
    db = sqlite3.connect('/home/kimsezin/DatabaseProject/Project/PetShop.db')
    db.row_factory = sqlite3.Row

    Client_items = db.execute(
        'select Phone_Number, Experience, Have_many, C_age, C_location'
        ' from Client'
    ).fetchall()
   
    Client_output = ""

    for item in Client_items:
        Client_output += item['Phone_Number']
        Client_output += item['Experience']
        Client_output += item['Have_many']
        Client_output += item['C_age']
        Client_output += item['C_location']  
    db.close()

    return render_template('Client.html')

@app.route("/Center")
def Center():
    db = sqlite3.connect('/home/kimsezin/DatabaseProject/Project/PetShop.db')
    db.row_factory = sqlite3.Row

    Center_items = db.execute(
        'select Center_Number, Location, Many_Pet, Grade, Pet_Hospital'
        ' from Center'
    ).fetchall()
   
    Center_output = ""

    for item in Center_items:
        Center_output += item['Center_Number']
        Center_output += item['Location']
        Center_output += item['Many_Pet']
        Center_output += item['Grade']
        Center_output += item['Pet_Hospital']
    
    db.close()

    return render_template('Center.html')
 
@app.route("/OK")
def OK():
    return render_template('OK.html')

@app.route("/Pet")
def Pet():
    return render_template('Pet.html')
if __name__ == "__main__":
    app.debug=True
    app.run(host='127.0.0.1',port=5001)
    