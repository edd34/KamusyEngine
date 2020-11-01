from app.language.models import Language
from app import db

def get_all_languages():
    """ Get all languages in the database"""
    all_languages = Language.query.order_by(Language.name).all()
    import pdb; pdb.set_trace()
    return [i.serialize for i in all_languages]

def get_language(language_id):
    """ Get language which id is given in param"""
    language = Language.query.filter_by(id=language_id).one()
    return language

def add_language(name):
    """ Add a language in the database"""
    language = Language(name=name)
    db.session.add(language)
    db.session.commit()
    result = {
        "id": language.id,
        "name": language.name,
        "date": language.date_created
    }
    return result