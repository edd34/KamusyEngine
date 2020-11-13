"""
    This is the main entry for KamusyEngine
"""
from app import create_app, enable_CORS, register_blueprint, init_db
from configparser import ConfigParser
DATABASE_URI = 'sqlite:///kamusy.db'

import json
with open('config.json', 'r') as f:
    config = json.load(f)

if __name__ == "__main__":
    app = create_app(DATABASE_URI)
    app.config.update(config["DEFAULT"])
    init_db(app)
    enable_CORS(app)
    register_blueprint(app)
    app.run(debug=True)
