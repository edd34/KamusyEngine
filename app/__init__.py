from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask
from flask_cors import CORS
from flask_compress import Compress
from flask_mail import Mail

db = SQLAlchemy()
ma = Marshmallow()

from app.language.urls import language_component
from app.word.urls import word_component
from app.translation.urls import translation_component
from app.auth.auth import register, login, auth

mail = Mail()
compress = Compress()


def create_app(db_uri):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SECRET_KEY'] = b'\xcc9\x8e\xd9\x12B-\x86\xb8\xb7A\x99\x08\xc7\xc6\xf3\x07\x87\xd8W\xa30\xee\x9a'
    compress.init_app(app)
    mail.init_app(app)
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
    bp_components = [language_component, word_component, translation_component, auth]
    for component in bp_components:
        app.register_blueprint(component)
