#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bson.json_util import dumps, loads, ObjectId
from src.core.databases import get_database_connection


def get_all_words():
    """ Get all words in  """
    all_words = get_database_connection().word.find()
    return json.loads(dumps(list(all_words)))


def get_word(word_id):
    """ Get a word which id is given in param  """
    word = get_database_connection().word.find({"_id": ObjectId(word_id)})
    return json.loads(dumps(list(word)))


def add_word(name):
    """ Get Add a word to the database  """
    word = get_database_connection().word.insert_one({"name": name})
