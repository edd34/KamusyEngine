from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app.translation.api import add_translation, get_all_translation
from app.auth.auth import token_required

translation_component = Blueprint("translation", __name__)

@cross_origin()
@translation_component.route('/translations', methods=['GET'])
def url_get_all_translation():
    results, code = get_all_translation()
    return jsonify(dict(results=results)), code

@cross_origin()
@translation_component.route('/translations', methods=['POST'])
def url_add_translation():
    body = request.get_json()
    print("body", body)
    result, code = add_translation(body)
    return jsonify(dict(result=result)), code

