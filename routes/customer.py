from asyncio.windows_events import NULL
from flask import Flask, jsonify, request, render_template, Response,Blueprint
from flask_mysqldb import MySQL
from http import HTTPStatus

from utils.db import db
from models.customerModel import Customer

# imports required to work properly
# define the blueprint


blueprint_customer = Blueprint(name="blueprint_customer", import_name=__name__)

@blueprint_customer.route('/customer',methods=['GET'])
def getAllUsers():
        customers = Customer.query.all()
        return jsonify([customer.to_dict() for customer in customers]), 200


@blueprint_customer.route('/customer/<int:id>', methods=['GET'])
def getUser(id):
    try:
        customer = Customer.query.get(id)
        print('Im ok')
        print(customer)
        return jsonify(customer.to_dict()), 201

    except:
        return 'Something went wrong', 500


@blueprint_customer.route('/customer', methods=['POST'])
def createUser():
    userParams = request.get_json()
    name = userParams['name']
    email = userParams['email']
    phone = userParams['phone']
    passwd = userParams['passwd']

    aux_product = Customer(name, email, phone, passwd)
    db.session.add(aux_product)
    db.session.commit()

    return jsonify('OK'), 201

@blueprint_customer.route('/customer/<int:id>', methods=['PUT'])
def updateUser(id):
    try:
        customerParams = request.get_json()
        customer = Customer.query.get(id)

        if (customerParams.get('name')):
            customer.name = customerParams['name']
        if (customerParams.get('email')):
            customer.email = customerParams['email']
        if (customerParams.get('phone')):
            customer.phone = customerParams['phone']
        if (customerParams.get('passwd')):
            customer.passw = customerParams['passwd']

        log_db = db.session.commit()

        return jsonify('OK'), 201

    except log_db as error:
        return error, 500

@blueprint_customer.route('/customer/<int:id>', methods=['DELETE'])
def deleteUser(id):
    try:
        customer = Customer.query.get(id)
        db.session.delete(customer)
        db.session.commit()
        return jsonify('OK'), 201

    except:
        return 'Something went wrong', 500
