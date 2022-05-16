from asyncio.windows_events import NULL
from flask import Flask, jsonify, request, render_template, Response, Blueprint,url_for,flash, make_response, flash, redirect, url_for, send_file
import json

from models.productModel import Product
from utils.db import db

from flask_mysqldb import MySQL
from http import HTTPStatus

from utils.db import db

# imports required to work properly
from flask_cors import cross_origin
from utils.middlewares import validate_token,token_required
from sqlalchemy.sql import text

import PIL
from PIL import Image
from werkzeug.utils import secure_filename
import os

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

@blueprint_product.route('/product/search',methods=['GET'])
def getProductsByName():
        data = request.args;
        nameProduct = data.get("nameProduct")
        idStore = data.get('storeId')

        statement = text('SELECT * FROM Product WHERE Product.name like "%' + str(nameProduct) + '%" AND Product.fStore = "' + str(idStore) + '"')
        print(statement)
        rs = db.session.execute(statement)

        sendData = []
        for product in rs:
            sendData.append({'id': product.id, 'name': product.name, 'product_img': product.product_img,
                             'price_per_kg': product.price_per_kg, 'price_per_unit': product.price_per_unit, 'price_per_pack': product.price_per_pack, 'packQuantity': product.packQuantity , 'fCategory': product.fCategory,
                             'fStore': product.fStore, 'methodsAllowed': product.methodsAllowed})

        print(sendData)
        return jsonify(sendData), 201

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
@cross_origin()
@token_required
def createProduct():
    productParams = request.get_json()
    name = productParams['name']
    product_img = "/"
    print(product_img)
    price_per_kg = productParams['price_per_kg']
    price_per_unit = productParams['price_per_unit']
    price_per_pack = productParams['price_per_pack']
    packQuantity = productParams['packQuantity']
    description = productParams['description']
    fCategory = productParams['fCategory']
    fStore = productParams['fStore']
    methodsAllowed = productParams['methodsAllowed']
    print('description')
    print(description)
    aux_product = Product(name, product_img, price_per_kg, price_per_unit, price_per_pack, packQuantity, fCategory, fStore, description, methodsAllowed)
    db.session.add(aux_product)
    db.session.commit()

    return jsonify({'id': aux_product.id}), 201

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
        if (productParams.get('price_per_unit')):
            product.price_per_unit = productParams['price_per_unit']
        if (productParams.get('price_per_pack')):
            product.price_per_pack = productParams['price_per_pack']
        if (productParams.get('packQuantity')):
            product.packQuantity = productParams['packQuantity']
        if (productParams.get('description')):
            product.description = productParams['description']
        if(productParams.get('fCategory')):
             product.fCategory = productParams['fCategory']
        if (productParams.get('fStore')):
            product.fStore = productParams['fStore']
        if (productParams.get('methodsAllowed')):
            product.methodsAllowed = productParams['methodsAllowed']

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

@blueprint_product.route('/product/store/<int:id>', methods=['GET'])
#@cross_origin()
def getAllProductsOfAStore(id):
    try:
        print('Im alive here!!!')
        productsOfStore = db.session.query(Product).filter(
            Product.fStore == id
        )

        if productsOfStore == NULL:
            return jsonify("No items found"), 405
        else:
            return jsonify([product.to_dict() for product in productsOfStore]), 201

    except:
        return 'Something went wrong', 500

@blueprint_product.route('/product/store', methods=['GET'])
#@cross_origin()
def getOneProductOfAStore():
    try:
        data = request.args;
        idProduct = data.get("idProduct")
        idStore = data.get('idStore')
        print('Im alive here!!!enwlkfnfe')
        print(idProduct)
        print(idStore)
        productOfStore = db.session.query(Product).filter(
            Product.id == idProduct and Product.fStore == idStore
        ).first()

        print(productOfStore)

        return jsonify([{'id': productOfStore.id, 'name': productOfStore.name, 'price_per_kg': productOfStore.price_per_kg,
                         'price_per_unit': productOfStore.price_per_unit, 'packQuantity': productOfStore.packQuantity, 'price_per_pack': productOfStore.price_per_pack,
                         'product_img': productOfStore.product_img, 'description': productOfStore.description,
                         'fStore': productOfStore.fStore, 'fCategory': productOfStore.fCategory, 'methodsAllowed': productOfStore.methodsAllowed}]), 201

    except:
        return 'Something went wrong', 500

@blueprint_product.route('/product/getid', methods=['GET'])
@cross_origin()
@token_required
def getProductId():

    data = request.args;
    name = data.get('name')
    fStore = data.get('fStore')

    productCreated = db.session.query(Product).filter(
    Product.name == name and Product.fStore == fStore
    ).first()

    return jsonify({'id' : productCreated.id}), 201



@blueprint_product.route('/product/store/<int:id>', methods=['DELETE'])
def deleteAllProductsFromStore(id):
    try:
        productsOfStore = db.session.query(Product).filter(
            Product.fStore == id
        )
        db.session.delete(productsOfStore)
        db.session.commit()
        return jsonify("Deleted successfully"), 201

    except:
        return 'Something went wrong', 500



@blueprint_product.route('/product/uploadImg', methods=['POST'])
@cross_origin()
def upload_file():
    print(request.files)
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "Bad Usage", 401

        file = request.files['file']

        imgName = file.filename.split('.')[0]
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        #f = open("../" + filename, "wb")
        #f.close()
        print(request.form)
        id = request.form.get('id')

        product = Product.query.get(id)

        tempPath = "../src/temp/"
        pathToSave = "../src/"
        urlToSave = "http://localhost:3000/api/v1/product/get_image/"
        tempFilename = str(product.id) + "_product.png"
        filename = str(product.id) + "_product"

        #Save the url src in DB
        product.product_img = urlToSave + filename
        print( urlToSave + filename )
        log_db = db.session.commit()

        rute = os.path.dirname(__file__)

        #Resize to 256x256 px
        #fileResized = file.resize((256,256))
        #Save it temporarily to resize it
        file.save(os.path.join(rute , tempPath + tempFilename))

        # Opens a image in RGB mode
        im = Image.open(os.path.join(rute , tempPath + tempFilename))

        #If image is not correct size we need to resize it
        print('AQUI ESTOY PRINTEANDO EL SIZE')
        print(im.size)
        if((im.size != (256,256))):

            # Size of the image in pixels (size of original image)
            # (This is not mandatory)
            width, height = im.size

            # Setting the points for cropped image
            #left = 4
            #top = height / 5
            #right = 154
            #bottom = 3 * height / 5

            # Cropped image of above dimension
            # (It will not change original image)
            #im1 = im.crop((left, top, right, bottom))
            newsize = (256, 256)
            im1 = im.resize(newsize)

            #Save the img
            im1.save(os.path.join(rute, pathToSave + filename) , 'png')
        else:
            # Image was correct size and we dont have to resize it
            im.save(os.path.join(rute, pathToSave + filename), 'png')



        return jsonify("OK"), 201
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@blueprint_product.route('/product/get_image/<string:img>')
def get_image(img):
   try:
    imgName = img.split('.')[0]
    rute = os.path.dirname(__file__)
    filename = (os.path.join(rute, '../src/' + imgName))

    return send_file(filename, mimetype='image/jpeg')

   except:
        return jsonify("No image found"), 500