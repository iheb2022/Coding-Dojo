from flask import render_template, redirect, request, session, flash # type: ignore
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt # type: ignore

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']


    if len(first_name) < 2 or not first_name.isalpha():
        flash("First name must be at least 2 characters and only letters.", "register")
        return redirect('/')
    if len(last_name) < 2 or not last_name.isalpha():
        flash("Last name must be at least 2 characters and only letters.", "register")
        return redirect('/')
    if len(password) < 8:
        flash("Password must be at least 8 characters.", "register")
        return redirect('/')
    if password != confirm_password:
        flash("Passwords do not match.", "register")
        return redirect('/')


    if User.get_by_email({'email': email}):
        flash("Email is already registered.", "register")
        return redirect('/')

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user_data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": hashed_password
    }
    user_id = User.save(user_data)
    session['user_id'] = user_id
    session['first_name'] = first_name

    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user = User.get_by_email({'email': email})
    if not user:
        flash("Invalid email or password.", "login")
        return redirect('/')

    if not bcrypt.check_password_hash(user.password, password):
        flash("Invalid email or password.", "login")
        return redirect('/')

    session['user_id'] = user.id
    session['first_name'] = user.first_name
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('success.html', first_name=session['first_name'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
