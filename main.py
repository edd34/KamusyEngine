"""
    This is the main entry for KamusyEngine
"""
# from app import create_app, enable_CORS, register_blueprint, init_db
from flask import Flask
from flask_pymongo import PyMongo
from configparser import ConfigParser
import json
from src.router import Router

with open('config.json', 'r') as f:
    config = json.load(f)

def create_app(db_uri):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SECRET_KEY'] = b'\xcc9\x8e\xd9\x12B-\x86\xb8\xb7A\x99\x08\xc7\xc6\xf3\x07\x87\xd8W\xa30\xee\x9a'
    compress.init_app(app)
    mail.init_app(app)
    return app

def enable_CORS(app):
    app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'
    CORS(app)

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/kamusy"
kamusy_db = PyMongo(app)
Router(app)

if __name__ == "__main__":
    app.run(debug=True)
