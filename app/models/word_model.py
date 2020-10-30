from datetime import datetime
from marshmallow import fields
from app import db, ma
from app.models import dump_datetime
from app.models.language_model import Languages

class Word(db.Model):
    """Represent a word in the dictionary"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    language_id = db.Column(db.Integer, db.ForeignKey('languages.id'), nullable=False)
    language = db.relationship('Languages', uselist=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<Word %r>' % self.id

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
           'id' : self.id,
           'date_created': dump_datetime(self.date_created),
           'language_id': self.language_id,
           'language'
           'name': self.name
        }

class WordShema(ma.Schema):
    """Word schema for validation with Marshmallow"""
    name = fields.String()
    language_id = fields.Integer()