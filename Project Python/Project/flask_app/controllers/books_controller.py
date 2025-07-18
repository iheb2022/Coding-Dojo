from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.book_model import Book
from flask_app.models.user_model import User
from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime

@app.route('/books')
def dashboard():
    if 'user_id' not in session:
        flash("Please log in to access this page", "danger")
        return redirect('/')
    
    user = User.get_by_id({'id': session['user_id']})
    if not user:
        session.clear()
        flash("Session expired. Please log in again.", "danger")
        return redirect('/')
    
    books = Book.get_all()
    
    query = """
    SELECT book_id FROM favorites 
    WHERE user_id = %(user_id)s;
    """
    favorites_result = connectToMySQL(Book.DB).query_db(query, {'user_id': session['user_id']})
    favorites = [fav['book_id'] for fav in favorites_result] if favorites_result else []
    
    return render_template("dashboard.html", user=user, books=books, favorites=favorites, now=datetime.now())

@app.route('/books/create', methods=['POST'])
def create_book():
    if 'user_id' not in session:
        return redirect('/')
    
    if not Book.validate_book(request.form):
        return redirect('/books')
    
    data = {
        "title": request.form["title"],
        "description": request.form["description"],
        "user_id": session["user_id"]
    }
    
    book_id = Book.save(data)
    
    if book_id:
        Book.add_favorite({
            "user_id": session["user_id"],
            "book_id": book_id
        })
        flash("Book created successfully!", "success")
    else:
        flash("Failed to create book. Please try again.", "danger")
    
    return redirect('/books')

@app.route('/books/<int:book_id>')
def view_book(book_id):
    if 'user_id' not in session:
        flash("Please log in to view book details", "danger")
        return redirect('/')
    
    user = User.get_by_id({'id': session['user_id']})
    if not user:
        session.clear()
        flash("Session expired. Please log in again.", "danger")
        return redirect('/')
    
    book = Book.get_by_id({"id": book_id})
    if not book:
        flash("Book not found", "danger")
        return redirect('/books')
    
    favorited_users = Book.get_favorited_users({"id": book_id})
    
    user_has_favorited = any(
        user.id == fav_user['id'] 
        for fav_user in favorited_users
    )
    
    return render_template(
        "book_detail.html", 
        user=user, 
        book=book,
        favorited_users=favorited_users,
        user_has_favorited=user_has_favorited,
        now=datetime.now()
    )

@app.route('/books/<int:book_id>/update', methods=['POST'])
def update_book(book_id):
    if 'user_id' not in session:
        return redirect('/')
    
    if not Book.validate_book(request.form):
        return redirect(f'/books/{book_id}')
    
    data = {
        "id": book_id,
        "title": request.form["title"],
        "description": request.form["description"]
    }
    
    Book.update(data)
    flash("Book updated successfully!", "success")
    return redirect(f'/books/{book_id}')

@app.route('/books/<int:book_id>/delete')
def delete_book(book_id):
    if 'user_id' not in session:
        return redirect('/logout')
    
    book = Book.get_by_id({'id': book_id})
    if not book or book.user_id != session['user_id']:
        flash("You can't delete this book.", "danger")
        return redirect('/books')

    query = "DELETE FROM favorites WHERE book_id = %(book_id)s;"
    connectToMySQL('books_db').query_db(query, {'book_id': book_id})

    Book.delete({'id': book_id})
    return redirect('/books')

@app.route('/books/<int:book_id>/favorite')
def add_favorite(book_id):
    if 'user_id' not in session:
        return redirect('/')
    
    query = """
    SELECT * FROM favorites 
    WHERE user_id = %(user_id)s AND book_id = %(book_id)s;
    """
    existing = connectToMySQL(Book.DB).query_db(query, {
        'user_id': session['user_id'],
        'book_id': book_id
    })
    
    if not existing:
        Book.add_favorite({
            "user_id": session["user_id"],
            "book_id": book_id
        })
        flash("Added to favorites!", "success")
    else:
        flash("This book is already in your favorites", "info")
    
    return redirect('/books')

@app.route('/books/<int:book_id>/unfavorite')
def remove_favorite(book_id):
    if 'user_id' not in session:
        return redirect('/')
    
    Book.remove_favorite({
        "user_id": session["user_id"],
        "book_id": book_id
    })
    flash("Removed from favorites", "info")
    return redirect('/books')