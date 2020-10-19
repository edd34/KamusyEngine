"""
    This is the main entry for KamusyEngine
"""
from app import create_app, enable_CORS, register_blueprint, init_db

DATABASE_URI = 'sqlite:///kamusy.db'

if __name__ == "__main__":
    app = create_app(DATABASE_URI)
    init_db(app)
    enable_CORS(app)
    register_blueprint(app)
    app.run(debug=True)
