from marshmallow import fields, ValidationError, validates
from app import ma
from app.language.models import Language


class LanguageSchema(ma.Schema):
    """This class is used for validation and serialization with Flask-Marshmallow"""
    name = fields.String(required=True)

    @validates("name")
    def validate_languagage_name(self, value):
        if Language.query.filter_by(name=value).first():
            raise ValidationError("This name already exists.")

    class Meta:
        fields = ['name']