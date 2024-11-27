from flask import Flask, render_template, request, redirect, url_for # type: ignore
from users_model import User

app = Flask(__name__)

@app.route('/users')
def index():
    users = User.get_all()
    return render_template('index.html', users=users)

@app.route('/user/<int:user_id>')
def read_one(user_id):
    user = User.find_by_id(user_id)
    return render_template('read_one.html', user=user)

@app.route('/user/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email']
        }
        user_id = User.create(data)
        return redirect(url_for('read_one', user_id=user_id))
    return render_template('create_user.html')

@app.route('/user/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.find_by_id(user_id)
    if request.method == 'POST':
        data = {
            "id": user_id,
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email']
        }
        User.update_user(data)
        return redirect(url_for('read_one', user_id=user_id))
    return render_template('edit_user.html', user=user)

@app.route('/user/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    User.delete_by_id(user_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)