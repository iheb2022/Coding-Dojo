from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self,data):
        self.id=data['id']
        self.names=data['names']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    
    @classmethod
    def get_all(cls):
        qurey="SELECT * FROM dojos;"
        result=connectToMySQL("dojos_and_ninjas_schema").query_db(qurey)
        list_of_dojos=[]
        for data in result:
            list_of_dojos.append(Dojo(data))
        return list_of_dojos

    @classmethod
    def add_one(cls,data):
        qurey="INSERT INTO dojos (names) VALUES(%(names)s);"
        result=connectToMySQL("dojos_and_ninjas_schema").query_db(qurey,data)
        return result
    
    @classmethod
    def get_one(cls,data):
        qurey="select * from dojos join ninjas on ninjas.dojo_id=dojos.id where dojos.id=%(id)s;"
        result=connectToMySQL("dojos_and_ninjas_schema").query_db(qurey,data)
        if len(result)==0:
            return None
        
        dojo=cls(result[0])
        dojo.ninjas=[]
        for row in result:
            data={
                **row, 
                "id":row['ninjas.id'],
                "first_name":row['first_name'],
                "last_name":row['last_name'],
                "age":row['age'],
                "created_at":row['created_at'],
                "updated_at":row['updated_at']
            }
            dojo.ninjas.append(Ninja(data))
        return