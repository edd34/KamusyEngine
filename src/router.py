# -*- coding: utf-8 -*-
from flask import jsonify, redirect, url_for, request
from flask_restful import Resource, Api
import time
from src.ping import Ping

#https://flask-restful.readthedocs.io/en/latest/quickstart.html
class Router:
    def __init__(self,app):
        self.app = app
        self.api = Api(self.app)
        self.api.add_resource(Ping, '/ping')