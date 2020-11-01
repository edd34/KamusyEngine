from app.tests.base_test import BaseTest

from app.models.word_model import Word
from app.models.language_model import Languages
from app.models.dict_model import Dict

from app.api.word_api import word_api_component

class TestWord(BaseTest):
    def test_add_word(self):
        assert(False)