from flask import Flask,render_template,request,session,redirect,flash
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
import json
from flask_login import LoginManager,UserMixin,login_user
from Email import send_email
from random import randint
app= Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testDB'


db = SQLAlchemy(app)
login_manager=LoginManager(app)
@login_manager.user_loader
class Student(db.Model): 
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

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST' :
        if request.form.get('email') and request.form.get('password'):
            session['email']=request.form.get('email')
            session['password']=request.form.get('password')
            data =Student.query.filter_by(email=request.form.get('email'))
            if data and data.password==session['password']:
                session['data'] = {'score1': data.player1_score, 'score2': data.player2_score,'player1':data.player1,'player2':data.player2}
                flash('you have been logged in')
                return redirect(url_for('game'))
            else :
                flash('incorrect user info')
                return redirect(url_for('index'))
        elif request.form.get('new_password'):
            session['new_password']=request.form.get('new_password')
            data =Student.query.filter_by(email=session['email_']).first()
            if data.email:
                data.password=session['new_password']
                session.pop('new_password', None)
                session.pop('email_',None)
            db.session.commit()
    return render_template("login.html")
@app.route('/email')
def email():
    return render_template('email.html')
@app.route('/reset', methods=['GET','POST'])
def reset():
    if request.method == 'POST' :
        session['email_']=request.form.get('email_')
        session['validation_message']=str(randint(100000,999999))
        data =Student.query.filter_by(email=request.form.get('email_')).first()
        print(data)
        if data :
            send_email(session['email_'],session['validation_message'])
            return render_template('reset.html')
        else :
            session.pop('email_')
            session.pop('validation_message')
            return render_template('email.html',error=True)
    return redirect(url_for('index'))
@app.route('/virefy', methods=['GET','POST'])
def virefy():
    if request.method == 'POST' :
            session['valid']=request.form.get('passvalid')
            if session.get('validation_message')==request.form.get('passvalid'):
                print("what the heck")
                session.pop('validation_message', None)
                session.pop('valid', None)
                return render_template('reset_new.html')
            else:
                session.pop('valid', None)
                return render_template('reset.html')
    return redirect(url_for('index'))
@app.route('/logout')
def logout():
    if 'data' in session:
        session.pop('data', None)
        session.pop('email', None)
        session.pop('password', None)
    else:
        session.pop('name', None)
        session.pop('email', None)
        session.pop('password', None)
        session.pop('confirm_password', None)
        session.pop('player1', None)
        session.pop('player2', None)
    session.clear()
    return redirect(url_for('index'))
@app.route('/singup', methods=['GET','POST'])
def singup():
    inv1=False
    inv2=False
    inv3=False
    if request.method == 'POST' and  not session.get("confirm_password"):
        session['name']=request.form.get('name')
        session['email']=request.form.get('email')
        session['password']=request.form.get('password')
        session['confirm_password']=request.form.get('confirm_password')
        print(session['name'])
        if len(session['name'])<4 or checkuser(session['name']):
            inv1=True
        if '@' not in session['email'] or checkemail(session['email']) or len(session['email'])<4:
            inv2=True
        if session['password']!=session['confirm_password']:
            inv3=True
        if inv1 or inv2 or inv3 :
            session.pop('name', None)
            session.pop('email', None)
            session.pop('password', None)
            session.pop('confirm_password', None)
            return render_template("singup.html",inv1=inv1,inv2=inv2,inv3=inv3)
        else:
            return redirect(url_for('players'))    
    else:
        if session.get('confirm_password'):
            session.pop('confirm_password')
        return render_template("singup.html",inv1=inv1,inv2=inv2,inv3=inv3)
def checkuser(a):
    data =Student.query.filter_by(name=a).first()
    if data:
        return True
    return False
def checkemail(a):
    data =Student.query.filter_by(email=a).first()
    if data:
        return True
    return False
@app.route('/<user_score>',methods=['POST'])
def indexout(user_score):
    user_scores = json.loads(user_score)
    if 'data' in session:
        data =Student.query.filter_by(email=session['email']).first()
        if data:
            data.player1_score=user_scores['player2']
            data.player2_score=user_scores['player1']
        else:
            return redirect(url_for('index'))
    elif 'name' in session:
        user1=Student(name=session['name'],email=session['email'],password=session['password'],\
                player1=session['player1'],player2=session['player2'],\
                player1_score=user_scores['player1'],player2_score=user_scores['player2'])
        db.session.add(user1)
    db.session.commit()
    print(Student.query.all())
    return 'done'



@app.route('/players', methods=['GET','POST'])
def players():
    if session.get('confirm_password'):
        session.pop('confirm_password',None)
    if 'name' in session and 'email' in session and 'password' in session:
        if request.method == 'POST':
            session['player1']=request.form.get('player1')
            session['player2']=request.form.get('player2')
            return redirect(url_for('game')) 
        else:
            return render_template('players.html')     
    else:
        return redirect(url_for('singup'))
    

@app.route('/Game')
def game():
    if 'player1' in session and 'player2' in session:
        user1= {'score1': 0, 'score2': 0,'player1':session['player1'],'player2':session['player2']}
        return render_template('retro.html',user=user1)
    elif 'email' in session and 'password' in session:
        user1= session['data']
        return render_template('retro.html',user=user1)
    else:
        return redirect(url_for('index'))
if (__name__=="__main__"):
    app.run(debug=True,port=5100)
    

    
    