# -*- coding: utf-8 -*-
from flask_restful import Resource, Api
from src.components.ping import Ping
from src.components.language.language_api import LanguageApi
from src.components.translation.translation_api import TranslationApi
from src.components.word.word_api import WordApi

#https://flask-restful.readthedocs.io/en/latest/quickstart.html
class Router:
    def __init__(self,app):
        self.app = app
        self.api = Api(self.app)
        self.api.add_resource(Ping, '/ping')
        self.api.add_resource(LanguageApi, '/language', '/language?id=<id>')
        self.api.add_resource(TranslationApi, '/translations')
        self.api.add_resource(WordApi, '/word', '/word?id=<id>')