from app import db, ma

class Translation(db.Model):
    """Perform association between 2 words in different languages"""
    id = db.Column(db.Integer, primary_key=True)
    word1_id = db.Column(db.Integer, db.ForeignKey('word.id'), nullable=False)
    word2_id = db.Column(db.Integer, db. ForeignKey('word.id'), nullable=False)
    word1 = db.relationship('Word', foreign_keys=[word1_id])
    word2 = db.relationship('Word', foreign_keys=[word2_id])

    @property
    def serialize(self):
        return {
            'id': self.id,
            'word_source': self.word1.serialize,
            'word_destination': self.word2.serialize
        }