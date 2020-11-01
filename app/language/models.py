from datetime import datetime
from app import db

class Language(db.Model):
    """Represent a language"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    words = db.relationship('Word', backref='language')
    def __repr__(self):
        return '<Language %r>' % self.id
    
    def __str__(self):
        return '<Language %r>' % self.name
    
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'date_created': self.date_created,
            'name': self.name,
            'words': [i.serialize for i in self.words]
        }
