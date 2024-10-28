from flask import Flask,render_template,session,request,redirect#type:ignore
app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route('/')
def render():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comment']=request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')   



if __name__=='__main__':
    app.run(debug=True)