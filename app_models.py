"""
    This file contains models used in the database
"""

from datetime import datetime
from marshmallow import fields
from .shared_models import db, ma, dump_datetime

class Word(db.Model):
    """Represent a word in the dictionary"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    language = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<Word %r>' % self.id

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
           'id' : self.id,
           'date_created': dump_datetime(self.date_created),
           'language': self.language,
           'name': self.name
        }

class WordShema(ma.Schema):
    """Word schema for validation with Marshmallow"""
    name = fields.String()
    language = fields.String()

class Languages(db.Model):
    """Represent a language"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<Language %r>' % self.id

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
           'id' : self.id,
           'date_created': dump_datetime(self.date_created),
           'name': self.name
        }

class LanuguageShema(ma.Schema):
    """Language schema for validation with Marshmallow"""
    name = fields.String()

class Dict(db.Model):
    """Perform association between 2 words in different languages"""
    id = db.Column(db.Integer, primary_key=True)
    id_word1 = db.Column(db.Integer, nullable=False)
    id_word2 = db.Column(db.Integer, nullable=False)

class DictSchema(ma.Schema):
    """Dict schema for validation with Marshmallow"""
    id_word1 = fields.Integer()
    id_word2 = fields.Integer()
