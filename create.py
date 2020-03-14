import os
import csv
from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ("postgres://bswicxpxnhjjjp:0f2376a3ad0bf820a304a55e070428afdbb48b5250b4288ea72f49567c50bdeb@ec2-54-247-125-38.eu-west-1.compute.amazonaws.com:5432/d27bmfn74a4fbt")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
