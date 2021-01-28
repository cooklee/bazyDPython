
from flask import Flask, request, render_template

from get_data import get_authors, get_books
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



if __name__ == '__main__':
    app.run()