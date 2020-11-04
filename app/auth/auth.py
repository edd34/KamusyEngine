from flask import Blueprint, current_app, jsonify, request
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

    if user is None or  user.verify_password(body["password"]) == False:
        return jsonify({
            'result': False,
            'redirect': None,
            'message': 'Wrong id or password',
        }), 403

    token = jwt.encode({
        'id': str(user.id),
        'exp': datetime.datetime.now() + datetime.timedelta(minutes=60)
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
    secret_key = str(current_app.config['SECRET_KEY'])
    user = User(user_name=body["user_name"], email=body["email"])

    User.query.filter_by(user_name=body["user_name"])

    user.password = body["password"]
    db.session.add(user)
    db.session.commit()

    return jsonify({
        'result': True,
    }), 200

def token_required(something):
    def wrap():
        try:
            token_passed = request.headers['TOKEN']
            SECRET_KEY = str(current_app.config['SECRET_KEY'])
            if token_passed != '' and token_passed != None:
                try:
                    data = jwt.decode(token_passed,SECRET_KEY, algorithms=['HS256'])
                    token_exp = datetime.datetime.fromtimestamp(data["exp"])
                    print(token_exp, datetime.datetime.now())
                    # print(token_exp < datetime.datetime.now())
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
