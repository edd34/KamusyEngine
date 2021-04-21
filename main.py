"""
    This is the main entry for KamusyEngine
"""
# from app import create_app, enable_CORS, register_blueprint, init_db
from flask import Flask
from flask_pymongo import PyMongo
from src.router import Router
app = Flask(__name__)
routing = Router(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
print(mongo.db)
from configparser import ConfigParser

import json
with open('config.json', 'r') as f:
    config = json.load(f)
print(config)

if __name__ == "__main__":
    Router(app)
    app.run(debug=True)
