from flask import Flask,render_template
app= Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    return render_template('retro.html')
if (__name__=="__main__"):
    app.run(debug=True,port=5000)