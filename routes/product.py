from asyncio.windows_events import NULL
from flask import Flask, jsonify, request, render_template, Response, Blueprint,url_for,flash, make_response


from models.productModel import Product
from utils.db import db

from flask_mysqldb import MySQL
from http import HTTPStatus

from utils.db import db

# imports required to work properly

# define the blueprint

blueprint_product = Blueprint(name="blueprint_product", import_name=__name__)

@blueprint_product.route('/product',methods=['GET'])
def getAllProducts():
        products = Product.query.all()
        product_array = []
        print(products[0].name)
        #for row in products:
            #product_array.append({'id': row[0], 'name': row[1], 'product_img': row[2], 'price_per_kg': row[3], 'fCategory': row[4]})

        return jsonify([product.to_dict() for product in products]), 200

@blueprint_product.route('/product/<int:id>', methods=['GET'])
def getProduct(id):
    try:
       product = Product.query.get(id)
       print('Im ok')
       print(product)
       return jsonify(product.to_dict()), 201

    except:
        return 'Something went wrong', 500

@blueprint_product.route('/product', methods=['POST'])
def createProduct():
    productParams = request.get_json()
    name = productParams['name']
    product_img = productParams['product_img']
    price_per_kg = productParams['price_per_kg']
    fCategory = productParams['fCategory']

    aux_product = Product(name, product_img, price_per_kg, fCategory)
    db.session.add(aux_product)
    db.session.commit()

    return jsonify('OK'), 201
    #return HTTPStatus.OK
@blueprint_product.route('/product/<int:id>', methods=['PUT'])
def updateProduct(id):
    try:
        productParams = request.get_json()
        product = Product.query.get(id)

        if(productParams.get('name')):
             product.name = productParams['name']
        if(productParams.get('product_img')):
             product.product_img = productParams['product_img']
        if(productParams.get('price_per_kg')):
             product.price_per_kg = productParams['price_per_kg']
        if(productParams.get('fCategory')):
             product.fCategory = productParams['fCategory']

        log_db = db.session.commit()

        return jsonify('OK'), 201

    except log_db as error:
        return error, 500

@blueprint_product.route('/product/<int:id>', methods=['DELETE'])
def deleteProduct(id):
    try:
       product = Product.query.get(id)
       db.session.delete(product)
       db.session.commit()
       return jsonify('OK'), 201

    except:
        return 'Something went wrong', 500
