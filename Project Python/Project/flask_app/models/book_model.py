from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Book:
    DB = 'books_db'

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.uploader = None

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO books (title, description, user_id)
        VALUES (%(title)s, %(description)s, %(user_id)s);
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = """
        SELECT books.*, users.first_name, users.last_name 
        FROM books
        JOIN users ON books.user_id = users.id
        ORDER BY books.created_at DESC;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        books = []
        for row in results:
            book = cls(row)
            book.uploader = f"{row['first_name']} {row['last_name']}"
            books.append(book)
        return books

    @classmethod
    def get_by_id(cls, data):
        query = """
        SELECT books.*, users.first_name, users.last_name 
        FROM books
        JOIN users ON books.user_id = users.id
        WHERE books.id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        if result:
            book = cls(result[0])
            book.uploader = f"{result[0]['first_name']} {result[0]['last_name']}"
            return book
        return None

    @classmethod
    def update(cls, data):
        query = """
        UPDATE books 
        SET title = %(title)s, description = %(description)s 
        WHERE id = %(id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM books WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def add_favorite(cls, data):
        query = """
        INSERT INTO favorites (user_id, book_id)
        VALUES (%(user_id)s, %(book_id)s);
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def remove_favorite(cls, data):
        query = """
        DELETE FROM favorites 
        WHERE user_id = %(user_id)s AND book_id = %(book_id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_favorited_users(cls, data):
        query = """
        SELECT users.id, users.first_name, users.last_name 
        FROM favorites
        JOIN users ON favorites.user_id = users.id
        WHERE book_id = %(id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @staticmethod
    def validate_book(data):
        is_valid = True
        if len(data.get('title', '')) < 1:
            flash("Title is required.", "book_error")
            is_valid = False
        if len(data.get('description', '')) < 5:
            flash("Description must be at least 5 characters.", "book_error")
            is_valid = False
        return is_valid