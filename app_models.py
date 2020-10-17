from datetime import datetime
from marshmallow import fields, validate
from .shared_models import db, ma

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]

class Word(db.Model):
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
    name = fields.String()
    language = fields.String()

class Languages(db.Model):
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
    name = fields.String()

class Dict(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_word1 = db.Column(db.Integer, nullable=False)
    id_word2 = db.Column(db.Integer, nullable=False)

class DictSchema(ma.Schema):
    id_word1 = fields.Integer()
    id_word2 = fields.Integer()
