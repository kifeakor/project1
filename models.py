import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Books:
    def __init__(self,isbn,title,author,year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
class Users1:
    def __init__(self,email,password):
        self.email = email
        self.password = password

class Books(db.Model):
    __tablename__ = "bookstore2"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.VARCHAR, nullable=False)
    title = db.Column(db.VARCHAR, nullable=False)
    author = db.Column(db.VARCHAR, nullable=False)
    year = db.Column(db.VARCHAR, nullable=False)
class Users1(db.Model):
    __tablename__ = "users1"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.VARCHAR, nullable=False)
    password = db.Column(db.VARCHAR, nullable=False)
