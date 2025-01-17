from flask import session,request,render_template,redirect  # type: ignore
from flask_app import app
from flask_app.models.user_model import User
from flask import flash  # type: ignore

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/new/user",methods=["POST"])
def add_user():
    data={**request.form}
    is_valid=User.validate(data)
    if not is_valid:
        return redirect('/')
    elif User.get_by_email(data)!=None:
        flash("email already in database","email_data")
        return redirect("/")
    else:
        data["password"]=User.encrypt_string(data["password"])
        user_id=User.add_one(data)
        user_data={
            "id":user_id
        }
        current_user=User.get_one(user_data)
        session["user_id"]=current_user.id
        session["name"]=current_user.first_name
        return redirect('/recipes')


@app.route('/user/login',methods=["POST"])
def login():
    user=User.get_by_email(request.form)
    if user==None:
        return redirect("/")
    elif not(User.validate_password(user.password,request.form["password"])):
        return redirect("/")
    else:
        session["user_id"]=user.id
        session["name"]=user.first_name
        return redirect("/recipes")
    
