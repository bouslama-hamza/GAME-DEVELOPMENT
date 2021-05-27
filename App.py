from enum import unique
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testDB'
db = SQLAlchemy(app)

class Student(db.Model): 

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100),unique=True, nullable= False)
    email = db.Column(db.String(50))
    player1 = db.Column(db.String(100), nullable= False)
    player2 = db.Column(db.String(100), nullable= False)
    def __repr__(self):
        return f"Student('{self.name}','{self.email}','{self.player1}','{self.player2}')"
usera=[]

@app.route('/')
def index():
    return render_template("Sign.html")

@app.route('/players', methods=['GET','POST'])
def players():
    
    global usera
    usera=[request.form['name'],request.form['email']]
    return render_template("players.html")

@app.route('/game', methods=['GET','POST'])
def game():

    global user1
    user1=Student(name=usera[0],email=usera[1],player1=request.form['player1'],player2=request.form['player2'])
    db.session.add(user1)
    db.session.commit()
    print(Student.query.all())
    return render_template('retro.html')

if (__name__=="__main__"):
    app.run(debug=True,port=8456)