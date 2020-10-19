from flask_testing import TestCase

from flask import Flask
from flask_testing import TestCase
from app import create_app, enable_CORS, register_blueprint, init_db


class BaseTest(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    TESTING = True

    def create_app(self):
        app = create_app(self.SQLALCHEMY_DATABASE_URISQLA)
        app.config['TESTING'] = True
        register_blueprint(app)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):

        db.session.remove()
        db.drop_all()