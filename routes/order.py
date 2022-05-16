from asyncio.windows_events import NULL
from typing import OrderedDict
from flask import Flask, jsonify, request, render_template, Response,Blueprint
from flask_mysqldb import MySQL
from http import HTTPStatus

from models.orderModel import Orden
from models.orderItemModel import Ordenitem
from models.productModel import Product
from utils.db import db
# imports required to work properly
# define the blueprint
from datetime import date
from utils.middlewares import validate_token,token_required
from flask_cors import cross_origin

import datetime as dt

import json
from sqlalchemy.sql import text

blueprint_order = Blueprint(name="blueprint_order", import_name=__name__)

@blueprint_order.route('/order',methods=['GET'])
#@cross_origin()
@token_required
def getAllOrdersFromCustomer():
    data = request.args;
    idCustomer = data.get("idCustomer")

    orders = db.session.query(Orden).filter(
            Orden.fCustomer == idCustomer
        ).order_by(Orden.order_date.desc())

    return jsonify([order.to_dict() for order in orders]), 200

@blueprint_order.route('/order/top',methods=['GET'])
#@cross_origin()
@token_required
def getMostFrequentedOrdersFromCustomer():
    data = request.args;
    idCustomer = data.get("idCustomer")

    orders = db.session.query(Orden).filter(
            Orden.fCustomer == idCustomer
        ).order_by(Orden.times_ordered.desc())

    return jsonify([order.to_dict() for order in orders[:3]]), 200



@blueprint_order.route('/order', methods=['POST'])
#@cross_origin()
@token_required
def createOrder():
    orderParams = request.get_json()
    print('order_params')
    print(orderParams)
    print(orderParams['times_ordered'])
    print(dt.datetime.now())
    order_date = dt.datetime.now()
    estimated_total = orderParams['estimated_total']
    status = 'created'
    anotations = orderParams['anotations']
    fCustomer = orderParams['fCustomer']
    fStore = orderParams['fStore']
    timesOrdered = 0
    if(orderParams['times_ordered'] == 0 or orderParams['times_ordered'] > 0):
        print('Hola entré al if del times_ordered en el create')
        timesOrdered = orderParams['times_ordered'] + 1

    print(timesOrdered)

    newOrden = Orden(order_date,estimated_total,status, anotations, timesOrdered, fCustomer,fStore)
    db.session.add(newOrden)
    db.session.commit()

    return jsonify({'id': newOrden.id}), 201

    #return HTTPStatus.OK

@blueprint_order.route('/order/<int:id>', methods=['PUT'])
#@cross_origin()
@token_required
def updateOrder(id):
    orderParams = request.get_json()
    order = Orden.query.get(id)

    if (orderParams.get('order_date')):
        order.order_date = orderParams['order_date']
    if (orderParams.get('estimated_total')):
        order.estimated_total = orderParams['estimated_total']
    if (orderParams.get('status')):
        order.status = orderParams['status']
    if (orderParams.get('anotations')):
        order.status = orderParams['anotations']
    if (orderParams.get('times_ordered')):
        order.times_ordered = orderParams['times_ordered']
    if (orderParams.get('fCustomer')):
        order.fCustomer = orderParams['fCustomer']
    if (orderParams.get('fStore')):
        order.fStore = orderParams['fStore']

    log_db = db.session.commit()

    return jsonify('OK'), 201

@blueprint_order.route('/order/<int:id>', methods=['DELETE'])
#@cross_origin()
@token_required
def deleteOrder(id):
    try:
        print(id)
        print('DELETE ORDER')
        order = Orden.query.get(id)
        print('DELETE ORDER 0.5')

        #Delete the sub items of the order
        statement = text('DELETE FROM Ordenitem WHERE Ordenitem.ordenId =' + str(id))
        print(statement)
        rs = db.session.execute(statement)
        
        print(rs)
        print('DELETE ORDER1')

        #Delete the order
        db.session.delete(order)
        print('DELETE ORDER2')

        db.session.commit()
        print('DELETE ORDER3')

        return jsonify('OK'), 201

    except:
        return 'Something went wrong', 500

@blueprint_order.route('/order/full',methods=['GET'])
#@cross_origin()
@token_required
def getAllOrdersFromCustomerFull():
    print('aquiiiiiiiiiiiiiiiiiiiiiiii')
    data = request.args;
    idCustomer = data.get("idCustomer")
    jsonData = json.loads(json.dumps({"orders": []}))
    print('aquiiiiiiiiiiiiiiiiiiiiiiii')

    #Orders from customer
    orders = db.session.query(Orden).filter(
            Orden.fCustomer == idCustomer
        ).all()
    print('aquiiiiiiiiiiiiiiiiiiiiiiii')

    print(orders)

    #Items for every order
    for indexOrder,order in enumerate(orders):
        print('Hellow')
        jsonOrder = json.loads(json.dumps(order.to_dict()))
        jsonOrder['items'] = []


        items = db.session.query(Ordenitem).filter(
            Ordenitem.ordenId == order.id
        ).all()
        print(items)

        #Get full info of the product
        for index,item in enumerate(items):

            #product = db.session.query(Product).filter(
            # Product.id == item.productId
            # ).first()
            statement = text('SELECT * FROM Product WHERE Product.id =' + str(item.productId))
            print(statement)
            rs = db.session.execute(statement)
            print('aqui productItemRefer')
            print(jsonData)
            print(rs)
            for product in rs:
                print(product)
            itemLoaded = json.loads(json.dumps(item.to_dict()))
            itemLoaded['productData'] = {'id': product.id, 'name': product.name, 'product_img': product.product_img,
                             'price_per_kg': product.price_per_kg, 'price_per_unit': product.price_per_unit, 'price_per_pack': product.price_per_pack, 'packQuantity': product.packQuantity , 'fCategory': product.fCategory,
                             'fStore': product.fStore, 'methodsAllowed': product.methodsAllowed}
            print(itemLoaded)


            jsonOrder['items'].append(itemLoaded)

        jsonData['orders'].append(jsonOrder)
    print(jsonData)


    return jsonData, 201



@blueprint_order.route('/order/receivedStore',methods=['GET'])
#@cross_origin()
@token_required
def getAllOrdersFromStoreFull():
    print('aquiiiiiiiiiiiiiiiiiiiiiiii')
    data = request.args;
    idStore = data.get("idStore")
    print('aqui el idStore')
    print(idStore)
    jsonData = json.loads(json.dumps({"orders": []}))
    print('aquiiiiiiiiiiiiiiiiiiiiiiii')

    #Orders from customer
    orders = db.session.query(Orden).filter(
            Orden.fStore == idStore
        ).all()
    print('aquiiiiiiiiiiiiiiiiiiiiiiii')

    print(orders)

    #Items for every order
    for indexOrder,order in enumerate(orders):
        print('Hellow')
        jsonOrder = json.loads(json.dumps(order.to_dict()))
        jsonOrder['items'] = []


        items = db.session.query(Ordenitem).filter(
            Ordenitem.ordenId == order.id
        ).all()
        print(items)

        #Get full info of the product
        for index,item in enumerate(items):

            #product = db.session.query(Product).filter(
            # Product.id == item.productId
            # ).first()
            statement = text('SELECT * FROM Product WHERE Product.id =' + str(item.productId))
            print(statement)
            rs = db.session.execute(statement)
            print('aqui productItemRefer')
            print(jsonData)
            print(rs)
            for product in rs:
                print(product)
            itemLoaded = json.loads(json.dumps(item.to_dict()))
            itemLoaded['productData'] = {'id': product.id, 'name': product.name, 'product_img': product.product_img,
                             'price_per_kg': product.price_per_kg, 'price_per_unit': product.price_per_unit, 'price_per_pack': product.price_per_pack, 'packQuantity': product.packQuantity , 'fCategory': product.fCategory,
                             'fStore': product.fStore, 'methodsAllowed': product.methodsAllowed}
            print(itemLoaded)


            jsonOrder['items'].append(itemLoaded)

        jsonData['orders'].append(jsonOrder)
    print(jsonData)


    return jsonData, 201