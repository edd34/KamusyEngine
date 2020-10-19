from datetime import datetime
from marshmallow import fields
from app import db, ma
from app.models import dump_datetime

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