from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app.models import db, get_or_add
from app.models.word_model import Word
from app.models.language_model import Languages
from app.models.dict_model import Dict

dict_api_component = Blueprint("dict_api", __name__)

# dict api
@dict_api_component.route('/dicts', methods=['POST'])
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
@dict_api_component.route('/dicts', methods=['GET'])
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
