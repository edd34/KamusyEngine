from datetime import datetime
from app import db

class Word(db.Model):
    """Represent a word in the dictionary"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<Word %r>' % self.id

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
           'id' : self.id,
           'date_created': self.date_created,
           'language_id': self.language_id,
           'language': self.language.name,
           'name': self.name
        }
