import os

from flask import Flask, session, render_template, request, redirect
from flask_session import Session
from sqlalchemy import create_engine, text, ForeignKey
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship


app = Flask(__name__)

db_string = "postgres://bswicxpxnhjjjp:0f2376a3ad0bf820a304a55e070428afdbb48b5250b4288ea72f49567c50bdeb@ec2-54-247-125-38.eu-west-1.compute.amazonaws.com:5432/d27bmfn74a4fbt"
db = create_engine(db_string)
Base = declarative_base()

app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"] ="filesystem"


Session = sessionmaker(db)
session = Session()
class Review1(Base):
    __tablename__ = "reviews1"
    id = Column(Integer, primary_key=True)
    note = Column(String, nullable=True)
    username = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id',), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    users = relationship("User", back_populates="reviews1")
    books = relationship("Books", back_populates="reviews1")

    def __repr__(self):
        return "<users (note='%s', username ='%s')>"%(self.note, self.username)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    email = Column(String)
    password = Column(String)
    reviews1 = relationship("Review1", back_populates="users")
    def __repr__(self):
        #what will be returned when you query this table
        return "<User(name ='%s',email ='%s',password='%s')>"%(self.name,self.email,self.password)

class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    isbn = Column(String)
    title = Column(String)
    author = Column(String)
    year = Column(String)
    reviews1 = relationship("Review1", back_populates="books")
    def __repr__(self):
        return "<Books(isbn ='%s',title='%s', author ='%s', year ='%s')>"%(self.isbn,self.title,self.author,self.year)



Base.metadata.create_all(db)
