from flask import request,render_template,redirect # type: ignore
from flask_app.models.dojo import Dojo
from flask_app import app

@app.route("/")
def dojos():
    return redirect("/dojos")
@app.route("/dojos")
def get_dojos():
    list_of_dojos=Dojo.get_all()
    return render_template("dojos.html",list_of_dojos=list_of_dojos)

@app.route("/add/dojo",methods=["POST"])
def create_dojo():
    new_dojo={
        "names": request.form.get("names")
    }
    if not new_dojo["names"]:
        return render_template("dojos.html", list_of_dojos=Dojo.get_all(), error="Name cannot be empty.")
    Dojo.add_one(new_dojo)
    list_of_dojos = Dojo.get_all()
    return render_template("dojos.html",list_of_dojos=list_of_dojos)

@app.route("/ninja/form")
def ninja_form():
    list_of_dojos=Dojo.get_all()
    return render_template("ninja_form.html",list_of_dojos=list_of_dojos)

@app.route("/dojos/<int:id>")
def get_dojo(id):
    result=Dojo.get_one({"id":id})
    if result==None:
        return render_template("error.html")
    return render_template("show.html",dojo=result)