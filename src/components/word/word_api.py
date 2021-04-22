# -*- coding: utf-8 -*-
from flask_restful import reqparse, abort, Api, Resource

class WordApi(Resource):
    def get(self, id=None):
        return {"get all language": id}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='Rate to charge for this resource')
        parser.add_argument('language_id', type=str, help='Rate to charge for this resource')
        args = parser.parse_args(strict=True)
        return args