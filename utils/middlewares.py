from jwt import encode, decode
from jwt import exceptions
from os import getenv
from datetime import datetime, timedelta
from flask import jsonify
from functools import wraps
from flask import request
def expire_date(days: int):
    now = datetime.now()
    new_date = now + timedelta(days)
    return new_date


def getToken(data: dict):
    print('[middlewares | getToken]')
    print(data)
    token = encode(payload={**data, "exp": expire_date(1)},
                   key="1234", algorithm="HS256")
    return token.encode("UTF-8")


def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key="1234", algorithms=["HS256"])
        print("[middlewares | validate_token]")
        print(getenv("SECRET_KEY"))
        print(token)
        decode(token, key="1234", algorithms=["HS256"])
        print('after decoding in validate_token')

    except exceptions.DecodeError:
        response = jsonify({"message": "Invalid Token"})
        response.status_code = 401
        return response
    except exceptions.ExpiredSignatureError:
        response = jsonify({"message": "Token Expired"})
        response.status_code = 401
        return response


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
        if not token:
            return jsonify({'message' : 'Authorization required'}),401

        try:
            validate_token(token, output=False)
        except:
            return jsonify({'message: Invalid Token'}),401

        return f(*args, **kwargs)
    return decorated


