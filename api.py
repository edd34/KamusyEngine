from flask import Blueprint
from flask import Flask, render_template, url_for, request, redirect
from flask import jsonify
from .shared_models import db
from .app_models import Word

api_component = Blueprint("api", __name__)

@api_component.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        left_word = request.form['name']
        new_word = Word(name=left_word)

        try:
            db.session.add(new_word)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        words = Word.query.order_by(Word.date_created).all()
        return render_template('index.html', words=words)


@api_component.route('/delete/<int:id>')
def delete(id):
    word_to_delete = Word.query.get_or_404(id)
    try:
        db.session.delete(word_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that word'

@api_component.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    word = Word.query.get_or_404(id)

    if request.method == 'POST':
        word.name = request.form['name']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', word=word)

@api_component.route('/words/', methods=['GET'])
def get_all_words():
    words_query = Word.query.order_by(Word.name)
    json_list=[i.serialize for i in words_query.all()]
    return jsonify(json_list), 200

@api_component.route('/word/<int:id>', methods=['GET'])
def get_word(id):
    word = Word.query.filter_by(id=id).one()
    return jsonify(id=word.id, name=word.name, language=word.language, date=word.date_created), 200

@api_component.route('/word/', methods=['PSOT'])
def add_word(id):
    body = request.json()
    word = Word(name=body.name, language=body.language)
    db.session.add(word)
    db.session.commit()
    return jsonify(id=word.id, name=word.name, language=word.language, date=word.date_created), 200

@api_component.route('/word/<int:id>', methods=['UPDATE'])
def update_word(id):
    word = Word.query.filter_by(id=id).one()
    body = request.json()
    if body.name is not None:
        word.name = body.name
    if body.language is not None:
        word.language = body.language
    db.session.commit()
    return jsonify(id=word.id, name=word.name, language=word.language, date=word.date_created), 200

@api_component.route('/word/<int:id>', methods=['DELETE'])
def delete_word(id):
    Word.query.filter_by(id=id).delete()
    return jsonify(), 200