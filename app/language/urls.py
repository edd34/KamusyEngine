from flask import request, jsonify
from flask_cors import cross_origin
from app.language.api import get_all_languages, get_language, add_language
from app.language.serializers import LanguageSchema
from marshmallow import ValidationError
from flask import Blueprint

language_component = Blueprint("language_api", __name__)

@cross_origin()
@language_component.route('/languages/', methods=['GET'])
def url_get_all_word():
    all_languages = get_all_languages()
    return jsonify(dict(languages=all_languages)), 200

@cross_origin()
@language_component.route('/language/<int:language_id>', methods=['GET'])
def url_get_language(language_id):
    language = get_language(language_id)
    return jsonify(dict(language=language))

@cross_origin()
@language_component.route('/language/', methods=['POST'])
def url_add_language():
    try:
        data = LanguageSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify({"errors":err.messages}), 422
    res = add_language(data.get("name"))
    return jsonify(res), 200
