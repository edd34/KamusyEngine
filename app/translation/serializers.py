from marshmallow import fields, validates_schema, ValidationError
from app.translation.models import Translation
from app import ma

class TranslationSchema(ma.Schema):
    """Translation dict schema for validation with Marshmallow"""
    word1_id = fields.Integer()
    word2_id = fields.Integer()

    @validates_schema
    def validate_translation_schema(self, data, **kwargs):
        import pdb; pdb.set_trace()
        if Translation.query.filter_by(word1_id=data["word1_id"], word2_id=data["word2_id"]).first():
            raise ValidationError("This translation already exists")
