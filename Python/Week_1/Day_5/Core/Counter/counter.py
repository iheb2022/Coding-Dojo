from flask import Flask, render_template, redirect, session # type: ignore
app=Flask(__name__)
app.secret_key='supersecretkey' 

@app.route('/count')
def visit():
    if 'counter' in session :
        session['counter']+=1
    else:
        session['counter']=1
    return render_template('index.html')

@app.route('/destroy_session')
def delete():
    session.clear()
    return redirect('/count')


if __name__=='__main__':
    app.run(debug=True)