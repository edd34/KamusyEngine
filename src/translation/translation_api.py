# -*- coding: utf-8 -*-
from flask_restful import reqparse, abort, Api, Resource

class TranslationApi(Resource):
    def get(self):
        return {"get all language": "id"}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('word1', type=str)
        parser.add_argument('word2', type=str)
        parser.add_argument('language1_id', type=str)
        parser.add_argument('language2_id', type=str)
        args = parser.parse_args(strict=True)
        return args