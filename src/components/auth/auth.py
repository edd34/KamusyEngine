from flask import Blueprint, current_app, jsonify, request
from flask_mail import Message, Mail
from app.user.models import User
import datetime
from app import db
import jwt

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():

    body = request.get_json()

    secret_key = str(current_app.config['SECRET_KEY'])
    user = User.query.filter_by(email=body["email"]).first()

    # Check if user is confirmed for return is organisation and domain

    # if user.confirmed == False:
    #     return jsonify({
    #         'result': False,
    #         'redirect': '/InstantRecommendation',
    #         'message': 'User not confirmed yet',
    #         'user_email': user.email,
    #         'user_is_confirmed': False
    #     }), 403

    if user is None or user.verify_password(body["password"]) == False:
        return jsonify({
            'result': False,
            'redirect': None,
            'message': 'Wrong id or password',
        }), 403

    token = jwt.encode({
        'id': str(user.id),
        'exp': datetime.datetime.now() + datetime.timedelta(days=0.5)
    }, secret_key, algorithm='HS256')

    return jsonify({
        'result': True,
        'token': token
        # 'redirect': '/InstantRecommendation',
        # 'token': token.decode('UTF-8'),
    }), 200

@auth.route('/register', methods=['POST'])
def register():

    body = request.get_json()
    user = User.query.filter_by(email=body["email"]).first()
    if user:
        return jsonify({
        'result': False,
        'message': 'email already exists',
        'field': 'email'
        }), 409

    user = User.query.filter_by(user_name=body["user_name"]).first()
    if user:
        return jsonify({
        'result': "error",
        'message': 'username already exists',
        'field': 'user_name'
        }), 409

    secret_key = str(current_app.config['SECRET_KEY'])
    user = User(user_name=body["user_name"], email=body["email"])

    user.password = body["password"]
    db.session.add(user)
    db.session.commit()

    token = jwt.encode({'id': user.id}, secret_key, algorithm='HS256')

    mail = Mail(current_app)
    msg = Message(subject="Veuillez confirmer votre adresse email", recipients=[body["email"]])
    lien = "http://localhost:5000/#/confirm?token="+str(token)[2:-1]
    msg.html = "Bonjour, validez votre lien ici <a href='" + lien + "'>" + lien + "</a>"
    res = mail.send(msg)

    return jsonify({
        'result': True,
    }), 200

@auth.route('/confirm/<token>', methods=['GET'])
def confirm_email(token):
    SECRET_KEY = str(current_app.config['SECRET_KEY'])
    data = jwt.decode(token,SECRET_KEY, algorithms=['HS256'])
    user_id = data["id"]
    user = User.query.filter_by(id=user_id).first()
    if user.confirmed == False:
        user.confirmed = True
        db.session.commit()
        mail = Mail(current_app)
        msg = Message(subject="Confirmation adresse email", recipients=[user.email])
        msg.body = "Bonjour, votre adresse email a bien été confirmée"
        res = mail.send(msg)
        return_data = {
            "message": "success, account confirmed",
            "id": user_id
            }
        return jsonify(response=return_data), 200
    else:
        return_data = {
            "status": "warning",
            "message": "success, account already confirmed",
            }
        return jsonify(response=return_data), 409

def token_required(something):
    def wrap():
        try:
            token_passed = request.headers['TOKEN']
            SECRET_KEY = str(current_app.config['SECRET_KEY'])
            if token_passed != '' and token_passed != None:
                try:
                    data = jwt.decode(token_passed,SECRET_KEY, algorithms=['HS256'])
                    token_exp = datetime.datetime.fromtimestamp(data["exp"])
                    return something()
                except jwt.exceptions.ExpiredSignatureError:
                    return_data = {
                        "error": "1",
                        "message": "Token has expired"
                        }
                    return jsonify(response=return_data), 401
                except Exception as e:
                    return e
                    return_data = {
                        "error": "2",
                        "message": "Invalid Token"
                    }
                    return jsonify(response=return_data), 401
            else:
                return_data = {
                    "error" : "3",
                    "message" : "Token required",
                }
                return jsonify(response=return_data), 401
        except Exception as e:
            return_data = {
                "error" : "4",
                "message" : "An error occured"
                }
            return jsonify(response=return_data), 500
    return wrap
