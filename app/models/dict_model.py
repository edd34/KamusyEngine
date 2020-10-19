from marshmallow import fields
from app import db, ma

class Dict(db.Model):
    """Perform association between 2 words in different languages"""
    id = db.Column(db.Integer, primary_key=True)
    id_word1 = db.Column(db.Integer, nullable=False)
    id_word2 = db.Column(db.Integer, nullable=False)

class DictSchema(ma.Schema):
    """Dict schema for validation with Marshmallow"""
    id_word1 = fields.Integer()
    id_word2 = fields.Integer()
