from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from app.word.api import get_all_words, get_word, add_word
from app.word.serializers import WordShema
from marshmallow import ValidationError

word_component = Blueprint("word_api", __name__)

@word_component.route('/words', methods=['GET'])
@cross_origin()
def url_get_all_words():
    result = get_all_words()
    return jsonify(dict(results=result))

@word_component.route('/word/<int:word_id>', methods=['GET'])
@cross_origin()
def url_get_word(word_id):
    word = get_word(word_id)
    return jsonify(dict(results=word)), 200

@word_component.route('/word', methods=['POST'])
@cross_origin()
def url_add_word():
    try:
        data = WordShema().load(request.get_json())
    except ValidationError as err:
        return jsonify(dict(errors=err.messages)), 422
    result = add_word(data)
    return jsonify(dict(result=result)), 200
