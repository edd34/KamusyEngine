"""
    This is the main entry for KamusyEngine
"""
from app import create_app, register_blueprint

DATABASE_URI = 'sqlite:///kamusy.db'

if __name__ == "__main__":
    app = create_app(DATABASE_URI)
    app.run(debug=True)
