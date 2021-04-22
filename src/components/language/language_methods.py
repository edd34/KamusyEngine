#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bson.json_util import dumps, loads, ObjectId
from src.core.databases import get_database_connection

def get_all_languages():
    """ Get all languages in the database"""
    all_languages = get_database_connection().language.find({})
    return json.loads(dumps(list(all_languages)))

def get_language(language_id):
    """ Get language which id is given in param"""
    print(language_id)
    all_languages = get_database_connection().language.find({"_id":ObjectId(language_id)})
    return json.loads(dumps(list(all_languages)))

def add_language(name):
    """ Add a language in the database"""
    res = get_database_connection().language.insert_one({"name": name})
    return res