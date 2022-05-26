from asyncio.windows_events import NULL
from flask import Flask, jsonify, request, render_template, Response,Blueprint
from flask_mysqldb import MySQL
from http import HTTPStatus
from werkzeug.security import generate_password_hash,check_password_hash
from functools import wraps
from utils.db import db
from models.customerModel import Customer
from utils.middlewares import validate_token,token_required
from flask_cors import cross_origin
# imports required to work properly
# define the blueprint

#This imports middlewares which are going to be applied to endpoints
#import app

blueprint_customer = Blueprint(name="blueprint_customer", import_name=__name__)



#This will be called before any request to this endpoints, veryfing the token credentials
#@blueprint_customer.before_request
def check_token_middleware():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        print('Aqui')
        print(token)
        validate_token(token, output=False)
        print('finish validate')
        return jsonify('XD')
    except:
         return jsonify('Authorization required'), 400

@blueprint_customer.route('/customer',methods=['GET'])
#@cross_origin()
@token_required
def getAllUsers():
        customers = Customer.query.all()
        return jsonify([customer.to_dict() for customer in customers]), 200


@blueprint_customer.route('/customer/email',methods=['POST'])
@cross_origin()
@token_required
def getUserByEmail():
    try:
        print('getUserByEmail im here')
        data = request.get_json()
        email = data['email']
        print('debug customer')
        print(email)
        # Get customer from db
        dbCustomer = db.session.query(Customer).filter(
            Customer.email == email
        ).first()
        return jsonify(dbCustomer.to_dict()), 200
    except:
        return jsonify("Error"),501

@blueprint_customer.route('/customer/<int:id>', methods=['GET'])
#@cross_origin()
@token_required
def getUser(id):
    try:
        customer = Customer.query.get(id)
        print('Im ok')
        print(customer)
        return jsonify(customer.to_dict()), 201

    except:
        return 'Something went wrong', 500


@blueprint_customer.route('/customer', methods=['POST'])
@cross_origin()
#@token_required
def createUser():
    userParams = request.get_json()
    name = userParams['name']
    email = userParams['email']
    phone = userParams['phone']
    passwd = userParams['passwd']
    zip = userParams['zip']
    address = userParams['address']
    seller = userParams['seller']
    hash_passwd = generate_password_hash(passwd, method='sha256')
    aux_customer = Customer(name, email, phone, hash_passwd, zip,address, seller)
    db.session.add(aux_customer)
    db.session.commit()

    return jsonify('OK'), 201

@blueprint_customer.route('/customer/<int:id>', methods=['PUT'])
#@cross_origin()
@token_required
def updateUser(id):
    try:
        customerParams = request.get_json()
        customer = Customer.query.get(id)

        if (customerParams.get('name') and customerParams.get('name') != ""):
            customer.name = customerParams['name']
        if (customerParams.get('email') and customerParams.get('email') != ""):
            customer.email = customerParams['email']
        if (customerParams.get('phone') and customerParams.get('phone') != ""):
            customer.phone = customerParams['phone']
        if (customerParams.get('passwd') and customerParams.get('passwd') != ""):
            customer.passwd = generate_password_hash(customerParams['passwd'], method='sha256')
        if (customerParams.get('zip') and customerParams.get('zip') != ""):
            customer.zip = customerParams['zip']
        if (customerParams.get('address') and customerParams.get('address') != ""):
            customer.address = customerParams['address']
        if (customerParams.get('seller') and customerParams.get('seller') != ""):
            customer.seller = customerParams['seller']

        log_db = db.session.commit()
        print('updated user success')
        return jsonify('OK'), 201

    except log_db as error:
        return error, 500

@blueprint_customer.route('/customer/<int:id>', methods=['DELETE'])
#@cross_origin()
@token_required
def deleteUser(id):
    try:
        customer = Customer.query.get(id)
        db.session.delete(customer)
        db.session.commit()
        return jsonify('OK'), 201

    except:
        return 'Something went wrong', 500
