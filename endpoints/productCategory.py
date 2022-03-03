from asyncio.windows_events import NULL
from flask import Flask, jsonify, request, render_template, Response,Blueprint
from flask_mysqldb import MySQL
from http import HTTPStatus

from mysqlconnection import mysql

# imports required to work properly
# define the blueprint

blueprint_productCategory = Blueprint(name="blueprint_productCategory", import_name=__name__)

@blueprint_productCategory.route('/productCategory',methods=['GET'])
def getAllProductCategory():
        cur = mysql.connection.cursor()
        cur.execute('Select * from productCategory')
        data = cur.fetchall()
        productCategory_array = []
        for row in data:
            productCategory_array.append({'id': row[0], 'name': row[1]})

        return jsonify(productCategory_array), 200

@blueprint_productCategory.route('/productCategory/<int:id>', methods=['GET'])
def getProductCategory(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('Select * from productCategory where id = ' + str(id))
        data = cur.fetchone()
        return jsonify({'id': data[0], 'name': data[1]}), 201
    except:
        return 'Something went wrong', 500

@blueprint_productCategory.route('/productCategory', methods=['POST'])
def createProductCategory():
    productCategoryParams = request.get_json()
    name = productCategoryParams['name']
        
    cur = mysql.connection.cursor()
    cur.execute('insert into productCategory (name) values (%s)', (name))
    cur.connection.commit()
    return jsonify('OK'), 201

@blueprint_productCategory.route('/productCategory/<int:id>', methods=['PUT'])
def updateProductCategory(id):
    productCategoryParams = request.get_json()
    name = productCategoryParams['name']
 
    cur = mysql.connection.cursor()
    cur.execute('update productCategory set name=%s where id=%s', (name,id))
    cur.connection.commit()
    return jsonify('OK'), 201

@blueprint_productCategory.route('/productCategory/<int:id>', methods=['DELETE'])
def deleteProductCategory(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('delete from productCategory where id = ' + str(id))
        cur.connection.commit()        
        return jsonify('OK'), 201
    except:
        return 'Something went wrong', 500
