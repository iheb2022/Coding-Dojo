from mysqlconnection import connectToMySQL # type: ignore

class User:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    
    @classmethod
    def get_all(cls):
        query="SELECT * FROM users;"
        result=connectToMySQL("users_schema").query_db(query)
        list_of_users=[]
        for data in result:
            list_of_users.append(User(data))
        return list_of_users
    
    @classmethod
    def create(cls,data):
        query="INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
        result=connectToMySQL("users_schema").query_db(query,data)