from flask import Flask ,render_template,request,redirect # type: ignore
from users_model import User

app=Flask(__name__)

@app.route("/users")
def get_users():
    list_of_users=User.get_all()
    return render_template("users.html",list_of_users=list_of_users)

@app.route("/user/form")
def display_user_form():
    return render_template("user_form.html")

@app.route("/user/new",methods=["GET"])
def create_user():
    new_user={
        "first_name":request.form["user_first_name"],
        "last_name":request.form["user_last_name"],
        "email":request.form["user_email"]
    }
    result=User.create(new_user)
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)