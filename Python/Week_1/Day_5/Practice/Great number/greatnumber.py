from urllib import request
from flask import Flask, render_template, request ,redirect, session # type: ignore

app=Flask(__name__)
app.secret_key='supersecretkey' 
import random

@app.route('/')
def home():
    if 'num' not in session:
      session['num']=random.randint(1,100)
    return render_template('index.html')
    

@app.route('/guess)
def guess():
    session['guess']=int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')



if __name__=='__main__':
    app.run(debug=True)