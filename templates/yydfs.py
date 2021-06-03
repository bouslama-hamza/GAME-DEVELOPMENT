from flask import Flask,render_template,session,request,redirect,url_for

app= Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    if session.get('name'):
        session.pop('name', None)
        session.pop('pass', None)
        return redirect(url_for('index'))
    if request.method== 'POST' :
        session['name']=request.form.get('namg')
        session['pass']=request.form.get('pass')
        return redirect(url_for('game'))
    return render_template('index.html')
@app.route('/gamesggggg')
def game():
    return render_template('game.html')