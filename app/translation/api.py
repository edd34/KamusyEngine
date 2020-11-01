from flask import Blueprint, request, jsonify
from app import db
from app.helpers import get_or_add
from app.language.models import Language
from app.word.models import Word
from app.translation.models import Translation
from marshmallow import ValidationError
from app.translation.serializers import TranslationSchema

def add_translation(body):
    """ Add a translation in the database.
        A translation consists of an assocation between 2 words in 2 differents languages.
        If a word do not exists in the database, create it. Don't create a same word twice.
    """

    try:
        language1 = Language.query.filter_by(id=body["language1_id"]).first()
        language2 = Language.query.filter_by(id=body["language2_id"]).first()

        word1 = get_or_add(Word,name=body["word1"], language_id=language1.id)
        word2 = get_or_add(Word,name=body["word2"], language_id=language2.id)
        db.session.flush()
        if Translation.query.filter_by(word1_id=word1.id, word2_id=word2.id).first():
            raise ValidationError("This translation already exists")

        translation = Translation(word1_id=word1.id, word2_id=word2.id)
        data = TranslationSchema().load(translation)
    except ValidationError as err:
        db.session.rollback()
        return {"error":err.messages}, 422
    db.session.add(translation)
    db.session.commit()
    return translation.serialize, 200

def get_all_translation():
    """ Get all translation in the database"""
    translation_dict = Translation.query.all()
    return [i.serialize for i in translation_dict], 200
