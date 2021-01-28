
from flask import Flask, request, render_template

from get_data import get_authors, get_books, get_book_by_id
from insert_data_to_db import dodaj_autora, dodaj_ksiazke

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("base.html")

@app.route('/add_authors', methods=['GET', 'POST'])
def author():
    if request.method == 'POST':
        dodaj_autora(**request.form)
    autorzy = get_authors()
    return render_template("author.html", autorzy=autorzy)

@app.route('/add_books', methods=['GET', 'POST'])
def books():
    if request.method == 'POST':
        dodaj_ksiazke(**request.form)
    autorzy = get_authors()
    books = get_books()
    return render_template("book.html", autorzy=autorzy, books=books)

@app.route('/book/<int:id>', methods=['GET', 'POST'])
def book(id):
    book = get_book_by_id(id)
    # if request.method == 'POST':
    #     dodaj_ksiazke(**request.form)
    autorzy = get_authors()
    books = get_books()
    return render_template("book.html", autorzy=autorzy, books=books, b=book)



if __name__ == '__main__':
    app.run()