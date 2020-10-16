from flask import Blueprint
from flask import Flask, render_template, url_for, request, redirect
from .shared_models import db
from .app_models import Word

api_component = Blueprint("api", __name__)

@api_component.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        left_word = request.form['name']
        new_word = Word(name=left_word)

        try:
            # import pdb
            # pdb.set_trace()
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
