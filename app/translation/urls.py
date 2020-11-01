from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app.translation.api import add_translation, get_all_translation

translation_component = Blueprint("translation", __name__)

@translation_component.route('/translation', methods=['POST'])
@cross_origin()
def url_add_translation():
    body = request.get_json()
    result, code = add_translation(body)
    return jsonify(dict(result=result)), code

@translation_component.route('/translation', methods=['GET'])
@cross_origin()
def url_get_all_translation():
    results, code = get_all_translation()
    return jsonify(dict(results=results)), code