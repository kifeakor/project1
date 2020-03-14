import csv
import os
from flask import Flask, render_template, request, session
from flask_session import Session
from sqlalchemy import create_engine, text, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)

db_string = "postgres://bswicxpxnhjjjp:0f2376a3ad0bf820a304a55e070428afdbb48b5250b4288ea72f49567c50bdeb@ec2-54-247-125-38.eu-west-1.compute.amazonaws.com:5432/d27bmfn74a4fbt"
db = create_engine(db_string)
Base = declarative_base()
Session = sessionmaker(db)
session = Session()
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"] ="filesystem"

class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    isbn = Column(String)
    title = Column(String)
    author = Column(String)
    year = Column(String)
    def __repr__(self):
        return "<Books(isbn ='%s',title='%s', author ='%s', year ='%s')>"%(self.isbn,self.title,self.author,self.year)

def load():
    f = open("books.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        books = Books(isbn=isbn,title=title,author=author,year=year)
        session.add(books)
    session.commit()
if __name__ == "__main__":
    with app.app_context():
        load()
