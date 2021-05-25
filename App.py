from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testDB'
db = SQLAlchemy(app)
class Student(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable= False)
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10),  nullable= False)
    def __init__(self,name,email):
        self.name=name
        self.email=email
db.session.add ()
lBooks =db.ession.query(Book) #returns a Query object.
for oBook in lBooks:
    print oBook.name
@app.route('/', methods=['GET','POST'])
def index():
    return render_template('retro.html')
if (__name__=="__main__"):
    app.run(debug=True,port=5000)