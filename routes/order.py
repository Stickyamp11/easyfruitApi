from asyncio.windows_events import NULL
from typing import OrderedDict
from flask import Flask, jsonify, request, render_template, Response,Blueprint
from flask_mysqldb import MySQL
from http import HTTPStatus

from mysqlconnection import mysql

# imports required to work properly
# define the blueprint

blueprint_order = Blueprint(name="blueprint_order", import_name=__name__)

@blueprint_order.route('/order',methods=['GET'])
def getAllOrders():
        cur = mysql.connection.cursor()
        cur.execute('Select * from order')
        data = cur.fetchall()
        order_array = []
        for row in data:
            order_array.append({'id': row[0], 'order_date': row[1], 'estimated_total': row[2], 'fCustomer': row[3], 'fStore': row[4]})

        return jsonify(order_array), 201

@blueprint_order.route('/order/customer/<int:customer_id>', methods=['GET'])
def getOrdersOfCustomer(customer_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('Select * from order where fCustomer = ' + str(customer_id))
        data = cur.fetchall()
        order_array = []
        for row in data:
            order_array.append({'id': row[0], 'order_date': row[1], 'estimated_total': row[2], 'fCustomer': row[3], 'fStore': row[4]})
        return jsonify(order_array), 201
    except:
        return 'Something went wrong', 500


@blueprint_order.route('/order/<int:id>', methods=['GET'])
def getOrdersOfCustomer(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('Select * from order where id = ' + str(id))
        data = cur.fetchone()
        return jsonify({'id': str(data[0]), 'order_date': str(data[1]), 'estimated_total': str(data[2]), 
        'fCustomer': str(data[3]), 'fStore': str(data[4])}), 201
    except:
        return 'Something went wrong', 500
@blueprint_order.route('/order', methods=['POST'])
def createOrder():
    orderParams = request.get_json()
    order_date = orderParams['order_date']
    estimated_total = orderParams['estimated_total']
    fCustomer = orderParams['fCustomer']
    fStore = orderParams['fStore']       
    cur = mysql.connection.cursor()
    cur.execute('insert into order (order_date,estimated_total,fCustomer,fStore) values (%s,%s,%s,%s)', (order_date,estimated_total,fCustomer,fStore))
    cur.connection.commit()
    return jsonify('OK'), 201
    #return HTTPStatus.OK
@blueprint_order.route('/order/<int:id>', methods=['PUT'])
def updateOrder(id):
    orderParams = request.get_json()
    order_date = orderParams['order_date']
    estimated_total = orderParams['estimated_total']
    fCustomer = orderParams['fCustomer']
    fStore = orderParams['fStore']    
    cur = mysql.connection.cursor()
    cur.execute('update order set order_date=%s,estimated_total=%s,fCustomer=%s,fStore=%s where id=%s', (order_date,estimated_total,fCustomer,fStore, id))
    cur.connection.commit()
    return jsonify('OK'), 201

@blueprint_order.route('/order/<int:id>', methods=['DELETE'])
def deleteOrder(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('delete from order where id = ' + str(id))
        cur.connection.commit()        
        return jsonify('OK'), 201
    except:
        return 'Something went wrong', 500
@blueprint_order.route('/order/customer/<int:customer_id>', methods=['DELETE'])
def deleteAllOrderOfCustomer(customer_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('delete from order where fCustomer = ' + str(customer_id))
        cur.connection.commit()        
        return jsonify('OK'), 201
    except:
        return 'Something went wrong', 500
