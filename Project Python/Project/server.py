from flask_app import app

from flask_app.controllers import users_controller
from flask_app.controllers import books_controller

if __name__ == "__main__":
    app.run(debug=True)
