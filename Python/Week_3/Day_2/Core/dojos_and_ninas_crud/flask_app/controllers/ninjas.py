from flask import request ,redirect, render_template # type: ignore
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask_app import app

@app.route("/ninja/form")
def ninja_form_first():
    list_of_dojos = Dojo.get_all()
    return render_template("ninja_form.html", list_of_dojos=list_of_dojos)


@app.route("/ninja/new",methods=["POST"])
def create_ninja():
    new_ninja={
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "age":request.form["age"],
        "dojo_id":request.form["dojo"]
    }

    if not new_ninja["first_name"] or not new_ninja["last_name"] or not new_ninja["age"] or not new_ninja["dojo_id"]:
        list_of_dojos = Dojo.get_all()
        return render_template(
            "ninja_form.html",
            list_of_dojos=list_of_dojos,
            error="All fields are required to create a ninja."
        )

    Ninja.add_one(new_ninja)
    return redirect(f"/dojos/{new_ninja['dojo_id']}")