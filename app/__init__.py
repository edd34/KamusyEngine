from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

from flask import Flask
from flask_cors import CORS
from app.api.dict_api import dict_api_component
from app.api.language_api import language_api_component
from app.api.word_api import word_api_component
# from app import db

def create_app(db_uri):
    app = Flask(__name__)
    app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    CORS(app)
    db.init_app(app)
    register_blueprint(app)
    with app.app_context():
        db.create_all()
    return app

def register_blueprint(app):
    bp_components = [dict_api_component, language_api_component, word_api_component]
    for component in bp_components:
        app.register_blueprint(component)