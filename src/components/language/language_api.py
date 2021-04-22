# -*- coding: utf-8 -*-
from flask_restful import reqparse, abort, Api, Resource, request
from src.components.language.language_methods import get_language, get_all_languages, add_language

class LanguageApi(Resource):
    def get(self):
        args = request.args
        if args["id"] is None:
            return get_all_languages()
        return get_language(args["id"])

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='Rate to charge for this resource')
        args = parser.parse_args(strict=True)
        
        add_language(args["name"])
        return 200