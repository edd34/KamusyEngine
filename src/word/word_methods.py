from flask import request
from app import db
from app.word.models import Word


def get_all_words():
    """ Get all words in  """
    words_list = Word.query.order_by(Word.name).all()
    return [i.serialize for i in words_list]


def get_word(word_id):
    """ Get a word which id is given in param  """
    word = Word.query.filter_by(id=word_id).one()
    return word

def add_word(body):
    """ Get Add a word to the database  """
    word = Word(name=body["name"], language_id=body["language_id"])
    db.session.add(word)
    db.session.commit()
    return word.serialize
