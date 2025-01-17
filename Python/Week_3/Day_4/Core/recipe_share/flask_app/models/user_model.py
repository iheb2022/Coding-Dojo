from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_bcrypt import Bcrypt # type: ignore
from flask import flash # type: ignore
import re
DB = 'recipe_db'

bcrypt=Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self,data):
        self.id=data["id"]
        self.first_name=data["first_name"]
        self.last_name=data["last_name"]
        self.email=data["email"]
        self.password=data["password"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]

    @classmethod
    def add_one(cls,data):
        query="insert into users(first_name,last_name,email,password) values(%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        result=connectToMySQL(DB).query_db(query,data)
        return result

    @staticmethod
    def encrypt_string(text):
        encrypted_string=bcrypt.generate_password_hash(text)
        return encrypted_string
    
    @staticmethod
    def validate_password(text1,text2):
        if (not bcrypt.check_password_hash(text1,text2)):
            flash("wrong password","login_password_validation")
            return False
        else:
            return True
        
    @staticmethod
    def validate(data):
        first_name=data["first_name"]
        last_name=data["last_name"]
        email=data["email"]
        password=data["password"]
        password_confirmation=data["password_confirmation"]
        is_valid=True
        if len(first_name)<2:
            is_valid=False
            flash("First Name needs to have at least 3 characters","first_name_validation")
        if len(last_name)<2:
            is_valid=False
            flash("Last Name needs to be at least 3 characters","last_name_validation")
        if not EMAIL_REGEX.match(email): 
            flash("Invalid email address!","email_validation")
            is_valid = False
        if len(password)<8:
            is_valid=False
            flash("Password not strong enough","password_validation")
        if password!=password_confirmation:
            is_valid=False
            flash("Password and confirmation must be the same","password_validation")
        return is_valid
    
    @classmethod
    def get_one(cls,data):
        query="select * from recipe_db.users where id=%(id)s;"
        result=connectToMySQL(DB).query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def get_by_email(cls,data):
        query="select * from users where email=%(email)s;"
        result=connectToMySQL(DB).query_db(query,data)
        if len(result)==0:
            flash("user email not in the database","email_validation_login")
            return None
        else:
            return cls(result[0])
        
    