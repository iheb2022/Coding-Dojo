from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash # type: ignore
DB = 'recipe_db'

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.under = data['under']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.posted_by = ""

    @classmethod
    def update(cls, data):
        query = """
        UPDATE recipes 
        SET name = %(name)s, description = %(description)s, instructions = %(instructions)s,
        date = %(date)s, under = %(under)s
        WHERE id = %(id)s;
        """
        connectToMySQL(DB).query_db(query, data)



    @classmethod
    def get_all(cls):
        query = """
        SELECT recipes.*, users.first_name AS posted_by 
        FROM recipes 
        JOIN users ON recipes.user_id = users.id;
        """
        result = connectToMySQL(DB).query_db(query)  
        all_recipes = []
        for data in result:
            recipe = cls(data)
            recipe.posted_by = data["posted_by"]
            all_recipes.append(recipe)
        return all_recipes


    @classmethod
    def get_by_id(cls, id):
        query = """
        SELECT recipes.*, users.first_name AS posted_by 
        FROM recipes 
        JOIN users ON recipes.user_id = users.id 
        WHERE recipes.id = %(id)s;
        """
        data = {'id': id}
        result = connectToMySQL(DB).query_db(query, data)
        if result: 
            recipe = cls(result[0]) 
            recipe.posted_by = result[0]['posted_by']
            return recipe
        return None


    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO recipes (name, description, instructions, date, under, user_id) 
        VALUES (%(name)s, %(description)s, %(instructions)s, %(date)s, %(under)s, %(user_id)s);
        """
        result = connectToMySQL(DB).query_db(query, data) 
        return result

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['name']) < 3:
            is_valid = False
            flash('Name must be at least 3 characters long', "name")
        if len(data['description']) < 3:
            is_valid = False
            flash('Description must be at least 3 characters long', "description")
        if len(data['instructions']) < 3:
            is_valid = False
            flash('Instructions must be at least 3 characters long', "instructions")
        if not data['date']:
            is_valid = False
            flash('Date must not be blank', "date")
        return is_valid
    

    @classmethod
    def delete(cls, data):
        query = """
        DELETE FROM recipes WHERE id = %(id)s;
        """
        connectToMySQL(DB).query_db(query, data)

    