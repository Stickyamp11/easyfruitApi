from asyncio.windows_events import NULL
from flask import Flask, jsonify, request, render_template, Response,Blueprint
from flask_mysqldb import MySQL
from http import HTTPStatus

from models.storeModel import Store
from utils.db import db
# imports required to work properly
# define the blueprint

blueprint_store = Blueprint(name="blueprint_store", import_name=__name__)

@blueprint_store.route('/store',methods=['GET'])
def getAllStores():
    stores = Store.query.all()
    return jsonify([store.to_dict() for store in stores]), 200

@blueprint_store.route('/store/<int:id>', methods=['GET'])
def getStore(id):
    try:
        store = Store.query.get(id)
        print('Im ok')
        print(store)
        return jsonify(store.to_dict()), 201

    except:
        return 'Something went wrong', 500

@blueprint_store.route('/store', methods=['POST'])
def createStore():
    storeParams = request.get_json()
    address = storeParams['address']
    comercial_logo = storeParams['comercial_logo']
    name = storeParams['name']

    aux_store = Store(address, comercial_logo, name)
    db.session.add(aux_store)
    db.session.commit()
    return jsonify('OK'), 201

@blueprint_store.route('/store/<int:id>', methods=['PUT'])
def updateStore(id):
    try:
        storeParams = request.get_json()
        store = Store.query.get(id)

        if (storeParams.get('address')):
            store.name = storeParams['address']
        if (storeParams.get('comercial_logo')):
            store.product_img = storeParams['comercial_logo']
        if (storeParams.get('name')):
            store.price_per_kg = storeParams['name']

        log_db = db.session.commit()

        return jsonify('OK'), 201

    except log_db as error:
        return error, 500

@blueprint_store.route('/store/<int:id>', methods=['DELETE'])
def deleteStore(id):
    try:
        store = Store.query.get(id)
        db.session.delete(store)
        db.session.commit()
        return jsonify('OK'), 201

    except:
        return 'Something went wrong', 500
