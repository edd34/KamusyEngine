# -*- coding: utf-8 -*-
from flask_restful import reqparse, abort, Api, Resource, request
from src.components.word.word_methods import add_word, get_word, get_all_words

class WordApi(Resource):
    def get(self):
        args = request.args
        if not "id" in args.keys():
            return get_all_words()
        return get_word(args["id"])

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='Rate to charge for this resource')
        args = parser.parse_args(strict=True)
        add_word(args["name"])
        return 200