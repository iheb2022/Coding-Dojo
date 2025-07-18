from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app import bcrypt

class User:
    DB = 'books_db'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        data['password'] = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if result:
            return cls(result[0])
        return None

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if result:
            return cls(result[0])
        return None

    @staticmethod
    def validate_registration(data):
        is_valid = True
        if len(data['first_name']) < 2:
            flash("First name must be at least 2 characters.", "reg_error")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last name must be at least 2 characters.", "reg_error")
            is_valid = False
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(data['email']):
            flash("Invalid email address.", "reg_error")
            is_valid = False
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters.", "reg_error")
            is_valid = False
        if data['password'] != data['confirm']:
            flash("Passwords do not match.", "reg_error")
            is_valid = False
        if User.get_by_email({'email': data['email']}):
            flash("Email already registered.", "reg_error")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(data):
        is_valid = True
        if len(data['email']) == 0:
            flash("Email is required.", "login_error")
            is_valid = False
        if len(data['password']) == 0:
            flash("Password is required.", "login_error")
            is_valid = False
        return is_valid