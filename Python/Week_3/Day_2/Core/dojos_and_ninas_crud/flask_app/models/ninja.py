from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.id=data["id"]
        self.first_name=data["first_name"]
        self.last_name=data["last_name"]
        self.age=data["age"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.dojo_id=data["dojo_id"]


    @classmethod
    def add_one(cls,data):
        qurey="INSERT INTO ninjas (first_name,last_name,age,dojo_id) VALUES(%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
        result=connectToMySQL("dojos_and_ninjas_schema").query_db(qurey,data)
        return result