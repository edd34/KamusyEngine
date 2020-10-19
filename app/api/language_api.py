from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app.models import db, get_or_add
from app.models.word_model import Word
from app.models.language_model import Languages
from app.models.dict_model import Dict

language_api_component = Blueprint("language_api", __name__)

# Language API
@language_api_component.route('/languages/', methods=['GET'])
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


@language_api_component.route('/language/<int:language_id>', methods=['GET'])
@cross_origin()
def get_language(language_id):
    """ Get language which id is given in param"""
    language = Languages.query.filter_by(id=language_id).one()
    return jsonify(id=language.id, name=language.name, date=language.date_created), 200

@language_api_component.route('/language/', methods=['POST'])
def add_language():
    """ Add a language in the database"""
    body = request.get_json()
    language = Languages(name=body["name"])
    db.session.add(language)
    db.session.commit()
    return jsonify(id=language.id, name=language.name, date=language.date_created), 200

@language_api_component.route('/language/<int:language_id>', methods=['PATCH'])
@cross_origin()
def update_language(language_id):
    """ Update a language from the database"""
    language = Languages.query.filter_by(id=language_id).first()
    body = request.get_json()
    if body["name"] is not None:
        language.name = body["name"]
    db.session.commit()
    return jsonify(id=language.id, name=language.name, date=language.date_created), 200

@language_api_component.route('/language/<int:language_id>', methods=['DELETE'])
@cross_origin()
def delete_language(language_id):
    """ Delete a language from the database"""
    Languages.query.filter_by(id=language_id).delete()
    return jsonify(), 200