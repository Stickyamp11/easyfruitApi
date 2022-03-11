from asyncio.windows_events import NULL
from flask import Flask, jsonify, request, render_template, Response,Blueprint
from flask_mysqldb import MySQL
from http import HTTPStatus

from utils.db import db
from models.productCategoryModel import ProductCategory
# imports required to work properly
# define the blueprint

blueprint_productCategory = Blueprint(name="blueprint_productCategory", import_name=__name__)

@blueprint_productCategory.route('/productCategory',methods=['GET'])
def getAllProductCategory():
    productcategorys = ProductCategory.query.all()
    return jsonify([productcategory.to_dict() for productcategory in productcategorys]), 200

@blueprint_productCategory.route('/productCategory/<int:id>', methods=['GET'])
def getProductCategory(id):
    try:
        productcategory = ProductCategory.query.get(id)
        print('Im ok')
        print(productcategory)
        return jsonify(productcategory.to_dict()), 201

    except:
        return 'Something went wrong', 500


@blueprint_productCategory.route('/productCategory', methods=['POST'])
def createProductCategory():
    productCategoryParams = request.get_json()
    name = productCategoryParams['name']

    aux_productcategory = ProductCategory(name)
    db.session.add(aux_productcategory)
    db.session.commit()

    return jsonify('OK'), 201

@blueprint_productCategory.route('/productCategory/<int:id>', methods=['PUT'])
def updateProductCategory(id):
    try:
        productCategoryParams = request.get_json()
        product = ProductCategory.query.get(id)

        if (productCategoryParams.get('name')):
            product.name = productCategoryParams['name']

        log_db = db.session.commit()

        return jsonify('OK'), 201

    except log_db as error:
        return error, 500

@blueprint_productCategory.route('/productCategory/<int:id>', methods=['DELETE'])
def deleteProductCategory(id):
    try:
        productcategory = ProductCategory.query.get(id)
        db.session.delete(productcategory)
        db.session.commit()
        return jsonify('OK'), 201

    except:
        return 'Something went wrong', 500