from asyncio.windows_events import NULL
from typing import OrderedDict
from flask import Flask, jsonify, request, render_template, Response,Blueprint
from flask_mysqldb import MySQL
from http import HTTPStatus

from mysqlconnection import mysql

# imports required to work properly
# define the blueprint

blueprint_order = Blueprint(name="blueprint_order", import_name=__name__)

@blueprint_order.route('/orderitem/<int:order_id>',methods=['GET'])
def getAllItemsOfOneOrder(order_id):
        cur = mysql.connection.cursor()
        cur.execute('Select * from ordenitem where ordenId ='+ str(order_id) )
        data = cur.fetchall()
        orderItem_array = []
        for row in data:
            orderItem_array.append({'ordenId': row[0], 'productId': row[1]})

        return jsonify(orderItem_array), 201


@blueprint_order.route('/orderitem', methods=['POST'])
def createOrderItem():
    orderParams = request.get_json()
    ordenId = orderParams['ordenId']
    productId = orderParams['productId']      
    cur = mysql.connection.cursor()
    cur.execute('insert into ordenitem (ordenId,productId) values (%s,%s)', (ordenId,productId))
    cur.connection.commit()
    return jsonify('OK'), 201
    #return HTTPStatus.OK


@blueprint_order.route('/orderitem/<int:ordenId>/<int:productId>', methods=['DELETE'])
def deleteOrderItem(ordenId,productId):
    try:
        cur = mysql.connection.cursor()
        cur.execute('delete from orderitem where ordenId = ' + str(ordenId) + ' and productId = ' + str(productId))
        cur.connection.commit()        
        return jsonify('OK'), 201
    except:
        return 'Something went wrong', 500

@blueprint_order.route('/orderitem/order/<int:order_id>', methods=['DELETE'])
def deleteAllOrderItemOfOrder(order_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('delete from ordenitem where ordenId = ' + str(order_id))
        cur.connection.commit()        
        return jsonify('OK'), 201
    except:
        return 'Something went wrong', 500
