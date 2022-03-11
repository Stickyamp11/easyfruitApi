import json
from . import auth
from flask import make_response, jsonify
#from app.models.User import User

@auth.get('/login')
def login():
    results = User.query.all()
    return jsonify([result.to_dict() for result in results])
    data = {'test': 'hi'}
    response = make_response()
    response.status_code = 200
    response.mimetype = 'application/json'
    response.response = json.dumps(data)