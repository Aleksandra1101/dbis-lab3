from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("postgres", "postgresql")
db = SQLAlchemy(app)

class Author(db.Model):
    name = db.Column(db.String(64), primary_key=True)
    hometown = db.Column(db.String(64), index=True)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    year = db.Column(db.Integer)
    author = db.Column(db.String(64), db.ForeignKey('author.name'))


db.create_all()
db.session.commit()


@app.route('/delete_book/<id>')
def delete_book(id):
    dl = db.session.query(Book).get(id)
    db.session.delete(dl)
    db.session.commit()
    return redirect('/index')

@app.route('/delete_author/<name>')
def delete_author(name):
    delete_list = Book.query.filter_by(author=name).all()
    for delete1 in delete_list:
        db.session.query(Book).get(delete1.id)
        db.session.delete(delete1)
        db.session.commit()

    delete = db.session.query(Author).get(name)
    db.session.delete(delete)
    db.session.commit()
    return redirect('/index')


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    warning = ''

    authors = Author.query.all()
    books = Book.query.all()

    if request.method == 'POST':
        name = request.form.get('author_name')
        hometown = request.form.get('hometown')

        if name and hometown != '':
            try:
                add = Author(name=name, hometown=hometown)
                db.session.add(add)
                db.session.commit()
                return redirect('/index')
            except:
                warning = 'The author is already exists!'

        name = request.form.get('book_name')
        year = request.form.get('year')
        author = request.form.get('book_author')

        add = Book(name=name, year=year, author=author)

        list_br = []
        all = Author.query.all()
        for br in all:
            list_br.append(br.name)

        if name and year != '':
            if str(author) in list_br:
                db.session.add(add)
                db.session.commit()
                return redirect('/index')
            warning = "The author is not found"

    return render_template('index.html', authors=authors, books=books, warning=warning)


if __name__=="__main__":
    app.run()
