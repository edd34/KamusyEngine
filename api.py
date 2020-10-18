from flask import Blueprint
from flask import Flask, render_template, url_for, request, redirect
from flask_cors import CORS, cross_origin
from flask import jsonify
import json
from .shared_models import db, get_or_add
from .app_models import Word, Languages, Dict

api_component = Blueprint("api", __name__)

# Words API
@api_component.route('/words/', methods=['GET'])
@cross_origin()
def get_all_words():
    words_query = Word.query.order_by(Word.name)
    json_list=[i.serialize for i in words_query.all()]
    return jsonify(json_list), 200

@api_component.route('/word/<int:id>', methods=['GET'])
@cross_origin()
def get_word(id):
    word = Word.query.filter_by(id=id).one()
    return jsonify(id=word.id, name=word.name, language=word.language, date=word.date_created), 200

@api_component.route('/word/', methods=['POST'])
@cross_origin()
def add_word():
    body = request.get_json()
    word = Word(name=body["name"], language=body["language"])
    db.session.add(word)
    db.session.commit()
    return jsonify(id=word.id, name=word.name, language=word.language, date=word.date_created), 200

@api_component.route('/word/<int:id>', methods=['PATCH'])
@cross_origin()
def update_word(id):
    word = Word.query.filter_by(id=id).one()
    body = request.get_json()
    if body["name"] is not None:
        word.name = body["name"]
    if body["language"] is not None:
        word.language = body["language"]
    db.session.commit()
    return jsonify(id=word.id, name=word.name, language=word.language, date=word.date_created), 200

@api_component.route('/word/<int:id>', methods=['DELETE'])
@cross_origin()
def delete_word(id):
    Word.query.filter_by(id=id).delete()
    return jsonify(), 200

# Language API
@api_component.route('/languages/', methods=['GET'])
@cross_origin()
def get_all_languages():
    all_languages = Languages.query.order_by(Languages.name).all()
    res = []
    for l in all_languages:
        query = db.session.query(Languages, db.func.count(Word.id)).join(Languages, Word.language == Languages.id).filter_by(id =l.id).group_by(Word.language).first()
        if query == None:
            query = 0
        else:
            query = query[1]
        res.append(dict(language=l.serialize, count=query))
    return jsonify(res), 200


@api_component.route('/language/<int:id>', methods=['GET'])
@cross_origin()
def get_language(id):
    language = Languages.query.filter_by(id=id).one()
    return jsonify(id=language.id, name=language.name, date=language.date_created), 200

@api_component.route('/language/', methods=['POST'])
def add_language():
    body = request.get_json()
    language = Languages(name=body["name"])
    db.session.add(language)
    db.session.commit()
    return jsonify(id=language.id, name=language.name, date=language.date_created), 200

@api_component.route('/language/<int:id>', methods=['PATCH'])
@cross_origin()
def update_language(id):
    language = Languages.query.filter_by(id=id).first()
    body = request.get_json()
    if body["name"] is not None:
        language.name = body["name"]
    db.session.commit()
    return jsonify(id=language.id, name=language.name, date=language.date_created), 200

@api_component.route('/language/<int:id>', methods=['DELETE'])
@cross_origin()
def delete_language(id):
    Languages.query.filter_by(id=id).delete()
    return jsonify(), 200

# dict api
@api_component.route('/dicts', methods=['POST'])
@cross_origin()
def add_translation():
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
    res = []
    dict_id = Dict.query.all()
    print(dict_id)
    for id in dict_id:
        tmp = {}
        current_word = Word.query.filter_by(id=id.id_word1).first()
        current_word_language = Languages.query.filter_by(id=current_word.language).first()
        translated_word = Word.query.filter_by(id=id.id_word2).first()
        translated_word_language = Languages.query.filter_by(id=translated_word.language).first()
        tmp["current_word_name"] = current_word.name
        tmp["current_word_language"] = current_word_language.name
        tmp["translated_word_name"] = translated_word.name
        tmp["translated_word_language"] = translated_word_language.name
        
        res.append(tmp)
    return jsonify(res=res), 200