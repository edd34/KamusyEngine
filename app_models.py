from datetime import datetime
from marshmallow import fields, validate
from .shared_models import db, ma



class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    language = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<Word %r>' % self.id

class WordShema(ma.Schema):
    name = fields.String()
    language = fields.String()

class Languages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<Language %r>' % self.id

class LanuguageShema(ma.Schema):
    name = fields.String()

class Relation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_word1 = db.Column(db.Integer, nullable=False)
    id_word2 = db.Column(db.Integer, nullable=False)

class RelationShema(ma.Schema):
    id_word1 = fields.Integer()
    id_word2 = fields.Integer()
