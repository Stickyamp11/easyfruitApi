from asyncio.windows_events import NULL
from flask import Flask, jsonify, request, render_template, Response,Blueprint
from flask_mysqldb import MySQL
from http import HTTPStatus

from mysqlconnection import mysql

# imports required to work properly
# define the blueprint

blueprint_product = Blueprint(name="blueprint_product", import_name=__name__)

@blueprint_product.route('/product',methods=['GET'])
def getAllProducts():
        cur = mysql.connection.cursor()
        cur.execute('Select * from product')
        data = cur.fetchall()
        product_array = []
        for row in data:
            product_array.append({'id': row[0], 'name': row[1], 'product_img': row[2], 'price_per_kg': row[3], 'fCategory': row[4]})

        return jsonify(product_array), 200

@blueprint_product.route('/product/<int:id>', methods=['GET'])
def getProduct(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('Select * from product where id = ' + str(id))
        data = cur.fetchone()
        return jsonify({'id': str(data[0]), 'name': str(data[1]), 'product_img': str(data[2]), 
        'price_per_kg': str(data[3]), 'fCategory': str(data[4])}), 201
    except:
        return 'Something went wrong', 500

@blueprint_product.route('/product', methods=['POST'])
def createProduct():
    productParams = request.get_json()
    name = productParams['name']
    product_img = productParams['product_img']
    price_per_kg = productParams['price_per_kg']
    fCategory = productParams['fCategory']    
    cur = mysql.connection.cursor()
    cur.execute('insert into product (name,product_img,price_per_kg,fCategory) values (%s,%s,%s,%s)', (name,product_img,price_per_kg,fCategory))
    cur.connection.commit()
    return jsonify('OK'), 201
    #return HTTPStatus.OK
@blueprint_product.route('/product/<int:id>', methods=['PUT'])
def updateProduct(id):
    productParams = request.get_json()
    name = productParams['name']
    product_img = productParams['product_img']
    price_per_kg = productParams['price_per_kg']
    fCategory = productParams['fCategory']    
    cur = mysql.connection.cursor()
    cur.execute('update product set name=%s,product_img=%s,price_per_kg=%s,fCategory=%s where id=%s', (name,product_img,price_per_kg,fCategory,id))
    cur.connection.commit()
    return jsonify('OK'), 201

@blueprint_product.route('/product/<int:id>', methods=['DELETE'])
def deleteProduct(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('delete from product where id = ' + str(id))
        cur.connection.commit()        
        return jsonify('OK'), 201
    except:
        return 'Something went wrong', 500
