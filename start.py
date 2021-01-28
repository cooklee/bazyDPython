
from flask import Flask, request, render_template

from get_data import get_authors
from insert_data_to_db import dodaj_autora

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

if __name__ == '__main__':
    app.run()