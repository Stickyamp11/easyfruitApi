from asyncio.windows_events import NULL
from typing import OrderedDict
from flask import Flask, jsonify, request, render_template, Response,Blueprint
from flask_mysqldb import MySQL
from http import HTTPStatus
from models.orderItemModel import Ordenitem
from utils.db import db
# imports required to work properly
# define the blueprint
from utils.middlewares import validate_token,token_required
from flask_cors import cross_origin
blueprint_orderitem = Blueprint(name="blueprint_orderitem", import_name=__name__)

@blueprint_orderitem.route('/orderitem',methods=['GET'])
#@cross_origin()
@token_required
def getAllItemsOfOneOrder():
    data = request.args;
    idOrder = data.get("idOrder")

    orderItems = db.session.query(Ordenitem).filter(
        Ordenitem.ordenId == idOrder
    )

    return jsonify([item.to_dict() for item in orderItems]), 200


@blueprint_orderitem.route('/orderitem', methods=['POST'])
#@cross_origin()
@token_required
def createOrderItem():
    data = request.get_json()
    orden = data['ordenId']
    items = data['itemsFromOrder']
    print(items)
    print('items aquí')
    for orderItemParams in items:
        ordenId = orden
        productId = orderItemParams['id']
        methodSelected = orderItemParams['methodSelected']
        unitsToBuy = orderItemParams['unitsToBuy']
        estimated_price = orderItemParams['estimated_price']
        newitem = Ordenitem(ordenId, productId, methodSelected, unitsToBuy, estimated_price)
        db.session.add(newitem)

    db.session.commit()
    return jsonify('OK'), 201
    #return HTTPStatus.OK

