"""
    API endpoints are located in this file.
"""

from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from .shared_models import db, get_or_add
from .app_models import Word, Languages, Dict

api_component = Blueprint("api", __name__)

# Words API
@api_component.route('/words/', methods=['GET'])
@cross_origin()
def get_all_words():
    """ Get all words in  """
    words_query = Word.query.order_by(Word.name)
    json_list=[i.serialize for i in words_query.all()]
    return jsonify(json_list), 200

@api_component.route('/word/<int:word_id>', methods=['GET'])
@cross_origin()
def get_word(word_id):
    """ Get a word which id is given in param  """
    word = Word.query.filter_by(id=word_id).one()
    return jsonify(id=word.id, name=word.name, language=word.language, date=word.date_created), 200

@api_component.route('/word/', methods=['POST'])
@cross_origin()
def add_word():
    """ Get Add a word to the database  """
    body = request.get_json()
    word = Word(name=body["name"], language=body["language"])
    db.session.add(word)
    db.session.commit()
    return jsonify(id=word.id, name=word.name, language=word.language, date=word.date_created), 200

@api_component.route('/word/<int:word_id>', methods=['PATCH'])
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

@api_component.route('/word/<int:word_id>', methods=['DELETE'])
@cross_origin()
def delete_word(word_id):
    """ Delete a word from the database"""
    Word.query.filter_by(id=word_id).delete()
    return jsonify(), 200

# Language API
@api_component.route('/languages/', methods=['GET'])
@cross_origin()
def get_all_languages():
    """ Get all languages in the database"""
    all_languages = Languages.query.order_by(Languages.name).all()
    res = []
    for elem_language in all_languages:
        query = db.session.query(Languages, db.func.count(Word.id)) \
        .join(Languages, Word.language == Languages.id) \
        .filter_by(id =elem_language.id).group_by(Word.language).first()
        if query is None:
            query = 0
        else:
            query = query[1]
        res.append(dict(language=elem_language.serialize, count=query))
    return jsonify(res), 200


@api_component.route('/language/<int:language_id>', methods=['GET'])
@cross_origin()
def get_language(language_id):
    """ Get language which id is given in param"""
    language = Languages.query.filter_by(id=language_id).one()
    return jsonify(id=language.id, name=language.name, date=language.date_created), 200

@api_component.route('/language/', methods=['POST'])
def add_language():
    """ Add a language in the database"""
    body = request.get_json()
    language = Languages(name=body["name"])
    db.session.add(language)
    db.session.commit()
    return jsonify(id=language.id, name=language.name, date=language.date_created), 200

@api_component.route('/language/<int:language_id>', methods=['PATCH'])
@cross_origin()
def update_language(language_id):
    """ Update a language from the database"""
    language = Languages.query.filter_by(id=language_id).first()
    body = request.get_json()
    if body["name"] is not None:
        language.name = body["name"]
    db.session.commit()
    return jsonify(id=language.id, name=language.name, date=language.date_created), 200

@api_component.route('/language/<int:language_id>', methods=['DELETE'])
@cross_origin()
def delete_language(language_id):
    """ Delete a language from the database"""
    Languages.query.filter_by(id=language_id).delete()
    return jsonify(), 200

# dict api
@api_component.route('/dicts', methods=['POST'])
@cross_origin()
def add_translation():
    """ Add a translation in the database.
        A translation consists of an assocation between 2 words in 2 differents languages.
        If a word do not exists in the database, create it. Don't create a same word twice.
    """
    body = request.get_json()

    language1 = Languages.query.filter_by(id=body["id_language1"]).first()
    language2 = Languages.query.filter_by(id=body["id_language2"]).first()

    word1 = get_or_add(Word,name=body["word1"], language=language1.id)
    word2 = get_or_add(Word,name=body["word2"], language=language2.id)

    db.session.flush()

    translation = Dict(id_word1=word1.id, id_word2=word2.id)
    db.session.add(translation)
    db.session.commit()
    return jsonify(id=translation.id), 200

# dict api
@api_component.route('/dicts', methods=['GET'])
@cross_origin()
def get_all_translation():
    """ Get all translation in the database"""
    res = []
    dict_id = Dict.query.all()
    for elem_id in dict_id:
        tmp = {}
        current_word = Word.query.filter_by(id=elem_id.id_word1).first()
        current_word_language = Languages.query.filter_by(id=current_word.language).first()
        translated_word = Word.query.filter_by(id=elem_id.id_word2).first()
        translated_word_language = Languages.query.filter_by(id=translated_word.language).first()
        tmp["current_word_name"] = current_word.name
        tmp["current_word_language"] = current_word_language.name
        tmp["translated_word_name"] = translated_word.name
        tmp["translated_word_language"] = translated_word_language.name

        res.append(tmp)
    return jsonify(res=res), 200
