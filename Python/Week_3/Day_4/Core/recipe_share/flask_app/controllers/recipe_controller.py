from flask_app import app
from flask_app.models.recipe_model import Recipe
from flask import render_template, session, redirect, request # type: ignore
from flask_app.models.user_model import User

@app.route('/recipes')
def dashboard():
    if "user_id" not in session:
        return redirect('/')
    recipes = Recipe.get_all()
    return render_template("recipes.html", recipes=recipes)


@app.route("/recipes/new")
def recipes_new():
    if "user_id" not in session:
        return redirect('/')
    return render_template("new_recipe.html")


@app.route('/logout', methods=["POST"])
def logout():
    session.clear()
    return redirect('/')

@app.route('/recipe/create', methods=["POST"])
def add_recipe():
    if "user_id" not in session:
        return redirect('/')
    if Recipe.validate(request.form):
        data = {
            **request.form,
            "user_id": session["user_id"]
        }  
        Recipe.create(data)
        return redirect("/recipes")
    else:
        print("Validation failed") 
    return redirect("/recipes/new")

@app.route('/recipe/<int:id>/delete', methods=["POST"])
def delete_recipe(id):
    if "user_id" not in session:
        return redirect('/')
    Recipe.delete({"id": id})
    return redirect('/recipes')

@app.route('/recipes/<int:id>')
def view_recipe(id):
    if "user_id" not in session:
        return redirect('/')
    recipe = Recipe.get_by_id(id) 
    return render_template("view.html", recipe=recipe)

@app.route('/recipes/<int:id>/edit')
def edit_recipe(id):
    if "user_id" not in session:
        return redirect('/')
    recipe = Recipe.get_by_id(id)
    if recipe:
        return render_template("edit.html", recipe=recipe)
    else:
        return "Recipe not found", 404

@app.route('/recipes/<int:id>/update', methods=["POST"])
def update_recipe(id):
    if "user_id" not in session:
        return redirect('/')
    if Recipe.validate(request.form):
        data = {
            **request.form,
            "id": id
        }
        Recipe.update(data)
        return redirect('/recipes')
    return redirect(f'/recipes/{id}/edit')


