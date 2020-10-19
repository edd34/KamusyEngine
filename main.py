"""
    This is the main entry for KamusyEngine
"""

from flask import Flask
from flask_cors import CORS
from app.api.dict_api import dict_api_component
from app.api.language_api import language_api_component
from app.api.word_api import word_api_component
from app import db
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kamusy.db'
app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'
db.init_app(app)

bp_components = [dict_api_component, language_api_component, word_api_component]
for component in bp_components:
    app.register_blueprint(component)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
