from asyncio.windows_events import NULL
from flask import Flask, jsonify, request, render_template, Response,Blueprint
from flask_mysqldb import MySQL
from http import HTTPStatus

from mysqlconnection import mysql

# imports required to work properly
# define the blueprint

blueprint_store = Blueprint(name="blueprint_store", import_name=__name__)

@blueprint_store.route('/store',methods=['GET'])
def getAllStores():
        cur = mysql.connection.cursor()
        cur.execute('Select * from store')
        data = cur.fetchall()
        store_array = []
        for row in data:
            store_array.append({'id': row[0], 'address': row[1], 'comercial_logo': row[2], 'name': row[3]})

        return jsonify(store_array), 200

@blueprint_store.route('/store/<int:id>', methods=['GET'])
def getStore(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('Select * from store where id = ' + str(id))
        data = cur.fetchone()
        return jsonify({'id': data[0], 'address': data[1], 'comercial_logo': data[2], 'name': data[3]}), 201
    except:
        return 'Something went wrong', 500

@blueprint_store.route('/store', methods=['POST'])
def createStore():
    storeParams = request.get_json()
    address = storeParams['address']
    comercial_logo = storeParams['comercial_logo']
    name = storeParams['name']
        
    cur = mysql.connection.cursor()
    cur.execute('insert into store (address,comercial_logo,name) values (%s,%s,%s)', (address,comercial_logo,name))
    cur.connection.commit()
    return jsonify('OK'), 201

@blueprint_store.route('/store/<int:id>', methods=['PUT'])
def updateStore(id):
    storeParams = request.get_json()
    address = storeParams['address']
    comercial_logo = storeParams['comercial_logo']
    name = storeParams['name']   
    cur = mysql.connection.cursor()
    cur.execute('update store set name=%s,comercial_logo=%s,address=%s where id=%s', (name,comercial_logo,address,id))
    cur.connection.commit()
    return jsonify('OK'), 201

@blueprint_store.route('/store/<int:id>', methods=['DELETE'])
def deleteStore(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('delete from store where id = ' + str(id))
        cur.connection.commit()        
        return jsonify('OK'), 201
    except:
        return 'Something went wrong', 500
