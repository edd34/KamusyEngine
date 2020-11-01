from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask
from flask_cors import CORS
db = SQLAlchemy()
ma = Marshmallow()
from app.language.urls import language_component
from app.word.urls import word_component
from app.translation.urls import translation_component


def create_app(db_uri):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    return app

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return db

def enable_CORS(app):
    app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'
    CORS(app)

def register_blueprint(app):
    bp_components = [language_component, word_component, translation_component]
    for component in bp_components:
        app.register_blueprint(component)
