from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .api import api_component
from .shared_models import db, ma
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kamusy.db'
app.register_blueprint(api_component)
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    
    app.run(debug=True)
