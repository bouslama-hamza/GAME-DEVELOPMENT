from flask import Flask,render_template,request,session,redirect
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
import json
from flask_login import LoginManager,UserMixin,login_user
app= Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testDB'
db = SQLAlchemy(app)
login_manager=LoginManager(app)
@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(int(user_id))
class Student(db.Model,UserMixin): 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable= False)
    email = db.Column(db.String(50), nullable= False)
    password = db.Column(db.String(50), nullable= False)
    player1 = db.Column(db.String(100), nullable= False)
    player2 = db.Column(db.String(100), nullable= False)
    player1_score = db.Column(db.String(100),)
    player2_score = db.Column(db.String(100),)
    def __repr__(self):
        return f"Student('{self.id}','{self.name}','{self.email}','{self.password}','{self.player1}','{self.player2}','{self.player1_score}','{self.player2_score}')"
@app.route('/')
def index():
    return render_template("login.html")

@app.route('/singup')
def singup():
    return render_template("singup.html")
@app.route('/<user_score>',methods=['POST'])
def indexout(user_score):
    user_scores = json.loads(user_score)
    print(session['user'])
    data =Student.query.filter_by(email=session['user'][0]).first()
    if session['user'][0]==data.email:
        print(session['user'][0].player1_score,'-',session['user'][0].player2_score)
        data.player1_score=user_scores['player1']
        data.player2_score=user_scores['player2']
    else:
        user1=Student(name=session['user'][0],email=session['user'][1],password=session['user'][2],\
                player1=session['user'][3],player2=session['user'][4],\
                player1_score=user_scores['player1'],player2_score=user_scores['player2'])
        db.session.add(user1)
    db.session.commit()
    session.clear()
    print(Student.query.all())
    return 'done'



@app.route('/players', methods=['GET','POST'])
def players():            
    session['user']=[request.form.get('name'),request.form.get('email'),request.form.get('password')]
    print([request.form.get('name'),request.form.get('email'),request.form.get('password')])
    return render_template("players.html")

@app.route('/Game', methods=['GET','POST'])
def game():
    if request.method=='POST' :
        if request.form.get('player1') and request.form.get('player2'):
            session['user']+=[request.form.get('player1'),request.form.get('player2')] 
            user = {'score1': 0, 'score2': 0,'player1':session['user'][3],'player2':session['user'][4]}
        elif request.form.get('email') and request.form.get('password'):
            x=0
            session['user']+=[request.form.get('email'),request.form.get('password')] 
            data =Student.query.filter_by(email=request.form.get('email')).first() #returns a Query object.
            if data and data.password==request.form.get('password'):
                    #session['user']=data   :( :( :(
                    login_user(data)
                    user = {'score1': data.player1_score, 'score2': data.player2_score,'player1':data.player1,'player2':data.player2}
            else :
                print('incorrect user info')
                return redirect(url_for('index'))
    else :
        return 'nice hhhhhh!!!!!!!!!!!!'
    return render_template('retro.html',user=user)

    

if (__name__=="__main__"):
    app.run(debug=True,port=8464)