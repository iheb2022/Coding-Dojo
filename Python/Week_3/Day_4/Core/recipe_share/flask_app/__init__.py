from flask import Flask # type: ignore

app=Flask(__name__)
app.secret_key="secret_key"
DATABASE="recipe_db"