from flask import render_template, redirect, request, session, flash
from flask_app import app, bcrypt
from flask_app.models.user_model import User

@app.route('/')
def index():
    return render_template('register_login.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_registration(request.form):
        return redirect('/')
    
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password']
    }
    
    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect('/books')

@app.route('/login', methods=['POST'])
def login():
    if not User.validate_login(request.form):
        return redirect('/')
    
    user = User.get_by_email({'email': request.form['email']})
    
    if not user:
        flash("Invalid Email/Password", "login_error")
        return redirect('/')
    
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password", "login_error")
        return redirect('/')
    
    session['user_id'] = user.id
    return redirect('/books')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')