from asyncio.windows_events import NULL
from flask import Flask, jsonify, request, render_template, Response,Blueprint
from flask_mysqldb import MySQL
from http import HTTPStatus
from werkzeug.security import generate_password_hash,check_password_hash
from functools import wraps
from utils.db import db
from models.customerModel import Customer
from models.cartModel import Cart
from models.productModel import Product
from utils.middlewares import validate_token,token_required
from flask_cors import cross_origin

from sqlalchemy.sql import text

# imports required to work properly
# define the blueprint

#This imports middlewares which are going to be applied to endpoints
#import app

blueprint_cart = Blueprint(name="blueprint_cart", import_name=__name__)


#This will be called before any request to this endpoints, veryfing the token credentials
#@blueprint_customer.before_request
def check_token_middleware():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        print('Aqui')
        print(token)
        validate_token(token, output=False)
        print('finish validate')
        return jsonify('XD')
    except:
         return jsonify('Authorization required'), 400

@blueprint_cart.route('/cart/<int:customerId>',methods=['GET'])
#@cross_origin()
@token_required
def getAllProductsOfCartFromCustomer(customerId):
        statement = text("""SELECT Product.* FROM Product JOIN Cart WHERE Cart.productId = Product.id and Cart.customerId = """ + str(customerId))
        rs = db.session.execute(statement)

        sendData = []
        for product in rs:
            sendData.append({'id': product.id, 'name': product.name, 'product_img': product.product_img,
                             'description': product.description, 'price_per_kg': product.price_per_kg, 'price_per_unit': product.price_per_unit,
                             'packQuantity': product.packQuantity, 'price_per_pack': product.price_per_pack, 'fCategory': product.fCategory, 'fStore': product.fStore, 'methodsAllowed': product.methodsAllowed })

        print(sendData)
        return jsonify(sendData), 201

@blueprint_cart.route('/cart/total/<int:customerId>',methods=['GET'])
#@cross_origin()
@token_required
def getCounterOfCart(customerId):
        statement = text("""SELECT Count(Product.id) as counts FROM Product JOIN Cart WHERE Cart.productId = Product.id and Cart.customerId = """ + str(customerId))
        rs = db.session.execute(statement)
        print(rs)
        sendData = rs.scalar()

        print(sendData)
        return jsonify(sendData), 201




@blueprint_cart.route('/cart',methods=['POST'])
#@cross_origin()
@token_required
def insertProductInCard():
    try:
        print('insertCart im here')
        data = request.get_json()
        customerId = data['customerId']
        productId = data['productId']

        aux_cart = Cart(customerId, productId)
        db.session.add(aux_cart)
        db.session.commit()
        return jsonify("OK"), 201
    except:
        return jsonify("Error"),501

@blueprint_cart.route('/cart', methods=['DELETE'])
#@cross_origin()
@token_required
def deleteProductFromCart():
    try:
        data = request.get_json()
        customerId = data['customerId']
        productId = data['productId']


        #productCart = db.session.query(Cart).filter(
         #   Cart.customerId == customerId and Cart.productId == productId
        #).first()

        statement = text(
            'DELETE FROM Cart WHERE Cart.productId = ' + str(productId) + ' AND Cart.customerId = ' + str(
             customerId) )
        print(statement)
        rs = db.session.execute(statement)

        #db.session.delete(productCart)
        db.session.commit()
        return jsonify('OK'), 201

    except:
        return 'Something went wrong', 500

@blueprint_cart.route('/cart/all', methods=['DELETE'])
#@cross_origin()
@token_required
def deleteCart():
    try:
        data = request.get_json()
        customerId = data['customerId']
        print('cart1')
        productsToDeleteFromCart = db.session.query(Cart).filter(
            Cart.customerId == customerId
        )
        print('cart2')
        for item in productsToDeleteFromCart:
            print(item)
            print(item.productId)

            statement = text('DELETE FROM Cart WHERE Cart.customerId = ' + str(
                customerId) + ' AND Cart.productId = ' + str(item.productId) )
            print(statement)
            rs = db.session.execute(statement)

        print('cart3')
        db.session.commit()
        return jsonify('OK'), 201

    except:
        return 'Something went wrong', 500
