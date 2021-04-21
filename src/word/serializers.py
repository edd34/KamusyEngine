from marshmallow import fields, validates, validates_schema, ValidationError
from app import ma, db
from app.word.models import Word
from app.language.models import Language


class WordShema(ma.Schema):
    """Word schema for validation with Marshmallow"""
    name = fields.String(required=True)
    language_id = fields.Integer(required=True)
    
    @validates("language_id")
    def validate_language_id(self, value):
        if not Language.query.filter_by(id=value).first():
            raise ValidationError("This language id doesn't exist")

    @validates_schema
    def validate_language_name(self, data, **kwargs):

        if Word.query.filter_by(language_id=data["language_id"], name=data["name"]).first():
            raise ValidationError("This word already exists in this language.")

    class Meta:
        fields = ["id", "name", "language_id"]
