from flask import render_template, request, redirect   # type: ignore
from flask_app.models.user import User
from flask_app import app

@app.route("/users/")
def get_users():
    list_of_users=User.get_all()
    return render_template("users.html",list_of_users=list_of_users)

@app.route("/user/form/")
def display_user_form():
    return render_template("user_form.html")

@app.route("/user/new",methods=["POST"])
def create_user():
    new_user={
        "first_name":request.form["user_first_name"],
        "last_name":request.form["user_last_name"],
        "email":request.form["user_email"]
    }
    id=User.create(new_user)
    return redirect("/show/user/"+str(id))

@app.route("/show/user/<int:id>")
def get_user(id):
    data={
        "id":id
    }
    user=User.show(data)
    return render_template("show.html",user=user)

@app.route("/delete/user/<int:id>",methods=["POST"])
def delete_user(id):
    data={
        "id":id
    }
    User.delete_one(data)
    return redirect("/users/")

@app.route("/edit/form/<int:id>")
def edit_form(id):
    data={
        "id":id
    }
    user=User.show(data)
    return render_template("edit.html",user=user)

@app.route("/edit/user/<int:id>",methods=["POST"])
def edit(id):
    data={
        "id":id,
        "first_name":request.form["user_first_name"],
        "last_name":request.form["user_last_name"],
        "email":request.form["user_email"]
    }
    User.update(data)
    return redirect("/users")