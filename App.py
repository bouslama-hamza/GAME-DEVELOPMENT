from flask import Flask,render_template,request,session,jsonify
from flask_sqlalchemy import SQLAlchemy
import json
app= Flask(__name__)
app.config['SECRET_KEY']='my sec'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testDB'
db = SQLAlchemy(app)
class Student(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable= False)
    email = db.Column(db.String(50), nullable= False)
    player1 = db.Column(db.String(100), nullable= False)
    player2 = db.Column(db.String(100), nullable= False)
    player1_score = db.Column(db.String(100), nullable= False)
    player2_score = db.Column(db.String(100), nullable= False)
    def __repr__(self):
        return f"Student('{self.name}','{self.email}','{self.player1}','{self.player2}','{self.player1_score}','{self.player2_score}')"
@app.route('/')
def index():
    return render_template("Sign.html")
'''@app.route('/_add_numbers')
def add_numbers():
    return jsonify(result='hello there')'''
@app.route('/<user_score>',methods=['POST'])
def indexout(user_score):
    user_scores = json.loads(user_score)
    session['user']+=[user_scores['player1'],user_scores['player2']]
    print(session['user'])
    user1=Student(name=session['user'][0],email=session['user'][1],\
             player1=session['user'][2],player2=session['user'][3],\
             player1_score=session['user'][4],player2_score=session['user'][5])
    db.session.add(user1)
    db.session.commit()
    print(Student.query.all())
    return 'done'
@app.route('/players', methods=['GET','POST'])
def players():
    session['user']=[request.form.get('name'),request.form.get('email')]
    print([request.form.get('name'),request.form.get('email')])
    return render_template("players.html")

@app.route('/game', methods=['GET','POST'])
def game():
        user = {'score1': 0, 'score2': 0}
        session['user']+=[request.form['player1'],request.form['player2']]
        return render_template('retro.html',user=user)
if (__name__=="__main__"):
    app.run(debug=True,port=8456)