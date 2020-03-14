import os

from flask import Flask, session, render_template, request, redirect, flash
from flask import session as login_session
from flask_session import Session
from sqlalchemy import create_engine, text
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from tables import *


app = Flask(__name__)

db_string = "postgres://bswicxpxnhjjjp:0f2376a3ad0bf820a304a55e070428afdbb48b5250b4288ea72f49567c50bdeb@ec2-54-247-125-38.eu-west-1.compute.amazonaws.com:5432/d27bmfn74a4fbt"
db = create_engine(db_string)
base = declarative_base()
Session = scoped_session(sessionmaker(bind=db))
app.config['DEBUG'] = True
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"] ="filesystem"
app.secret_key = 'super secret key'
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

session = Session()
base.metadata.create_all(db)


# Check for environmen


# Set up database

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    return render_template("login.html")

@app.route("/register", methods=["POST"])
def register():
    return render_template("register.html")

@app.route("/submit",methods=["POST"])
def submit():
    email=request.form.get('email')
    password=request.form.get('password')
    name =request.form.get('name')
    users = User(name=name,email=email, password=password)
    session.add(users)
    session.commit()
    return render_template("login.html")

@app.route("/validation", methods=["POST"])
def validation():
    email=request.form.get('email')
    print(email)
    password=request.form.get('password')
    print(password)
    Session = sessionmaker(db)
    session = Session()
    users = session.query(User).filter_by(email=email, password=password).first()
    if users:
        login_session['username'] = users.name
        login_session['user_id']=users.id
        user_id=login_session['user_id']
        print(user_id)
        username = login_session['username']
        return render_template("search.html",username=username)
    elif users== None:
        return render_template("register.html")
@app.route("/signout", methods=["GET","POST"])
def signout():
    session.flush()
    return render_template("login.html")
@app.route("/title_search", methods=["POST"])
def title_search():
    title=request.form.get('title')
    books =session.query(Books).filter_by(title=title).all()
    for book in books:
        login_session['book_id']=book.id
    print(books)
    username = login_session['username']
    return render_template("book.html",username=username,book=books, author=title)

@app.route("/author_search", methods=["POST"])
def author_search():
    author=request.form.get('author')
    books =session.query(Books).filter_by(author=author).all()
    for book in books:
        login_session['book_id']=book.id
    print(books)
    username = login_session['username']
    return render_template("book.html",username=username, book=books,author=author)

@app.route("/reviews/<int:book_id>")
def reviews(book_id):
    book = session.query(Books).filter_by(id=book_id).all()
    print(book)
    username = login_session['username']
    rev= session.query(Review1).filter_by(book_id=book_id).all()
    if book:
        return render_template("review.html",rev=rev,username=username, book=book)
@app.route("/review", methods=["POST"])
def add():
    username = login_session['username']
    return render_template("write.html",username=username)
@app.route("/write", methods=["POST"])
def write():
    currentuser=login_session["user_id"]
    reviwer= login_session['username']
    note=request.form.get('review')
    re=Review1(note=note,username=reviwer,user_id= currentuser, book_id=login_session['book_id'])
    session.add(re)
    session.commit()
    return render_template("search.html")
