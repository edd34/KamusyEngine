from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app.models import db, get_or_add
from app.models.word_model import Word
from app.models.language_model import Languages
from app.models.dict_model import Dict

word_api_component = Blueprint("word_api", __name__)

# Words API
@word_api_component.route('/words/', methods=['GET'])
@cross_origin()
def get_all_words():
    """ Get all words in  """
    words_query = Word.query.order_by(Word.name)
    json_list=[i.serialize for i in words_query.all()]
    return jsonify(json_list), 200

@word_api_component.route('/word/<int:word_id>', methods=['GET'])
@cross_origin()
def get_word(word_id):
    """ Get a word which id is given in param  """
    word = Word.query.filter_by(id=word_id).one()
    return jsonify(id=word.id, name=word.name, language=word.language, date=word.date_created), 200

@word_api_component.route('/word/', methods=['POST'])
@cross_origin()
def add_word():
    """ Get Add a word to the database  """
    body = request.get_json()
    word = Word(name=body["name"], language=body["language"])
    db.session.add(word)
    db.session.commit()
    return jsonify(id=word.id, name=word.name, language=word.language, date=word.date_created), 200

@word_api_component.route('/word/<int:word_id>', methods=['PATCH'])
@cross_origin()
def update_word(word_id):
    """ Update a word in the database"""
    word = Word.query.filter_by(id=word_id).one()
    body = request.get_json()
    if body["name"] is not None:
        word.name = body["name"]
    if body["language"] is not None:
        word.language = body["language"]
    db.session.commit()
    return jsonify(id=word.id, name=word.name, language=word.language, date=word.date_created), 200

@word_api_component.route('/word/<int:word_id>', methods=['DELETE'])
@cross_origin()
def delete_word(word_id):
    """ Delete a word from the database"""
    Word.query.filter_by(id=word_id).delete()
    return jsonify(), 200