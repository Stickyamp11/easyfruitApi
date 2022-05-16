from re import split
from flask import Blueprint, request, jsonify
from utils.middlewares import getToken, validate_token
from models.customerModel import Customer
from utils.db import db
from flask_cors import cross_origin
from werkzeug.security import generate_password_hash,check_password_hash

blueprint_authentication = Blueprint(name="blueprint_authentication", import_name=__name__)


@blueprint_authentication.route("/auth", methods=["POST"])
#@cross_origin()
def auth():
    data = request.get_json()
    print(data)
    email = data['email']
    passwd = data['passwd']

    #Get customer from db
    dbCustomer = db.session.query(Customer).filter(
        Customer.email == email
    ).first()
    try:
        if check_password_hash(dbCustomer.passwd, passwd):
            print('[authentication | auth] Passwd coincide')
            print(getToken(data=data).decode("utf-8") )
            return jsonify({'token': getToken(data=data).decode("utf-8")}),200
        else:
            response = jsonify({"message": "Incorrect password"})
            response.status_code = 404
            return response
    except:
        response = jsonify({"message": "User not found"})
        response.status_code = 404
        return response


@blueprint_authentication.route("/verify/token")
#@cross_origin()
def verify():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token, output=True)