from asyncio.windows_events import NULL
from flask import Flask, jsonify, request, render_template, Response,Blueprint, flash, redirect, url_for, send_file
from flask_mysqldb import MySQL
from http import HTTPStatus
import os
from models.storeModel import Store
from utils.db import db
# imports required to work properly

from flask_cors import cross_origin



# define the blueprint

blueprint_store = Blueprint(name="blueprint_store", import_name=__name__)

@blueprint_store.route('/store',methods=['GET'])
def getAllStores():
    stores = Store.query.all()
    return jsonify([store.to_dict() for store in stores]), 200

@blueprint_store.route('/store/<int:id>', methods=['GET'])
@cross_origin()
def getStore(id):
    try:
        store = Store.query.get(id)
        print('Im ok')
        print(store)
        return jsonify(store.to_dict()), 201

    except:
        return 'Something went wrong', 500

@blueprint_store.route('/store/emailManager/<string:email>', methods=['GET'])
@cross_origin()
def getStoreByEmailOfManager(email):
    try:

        filteredData = db.session.query(Store).filter(
            Store.storemanager == email
        ).first()
        return jsonify(filteredData.to_dict()), 201

    except:
        return 'Something went wrong', 500

@blueprint_store.route('/store', methods=['POST'])
def createStore():
    storeParams = request.get_json()
    address = storeParams['address']
    comercial_logo = storeParams['comercial_logo']
    name = storeParams['name']
    phone = storeParams['phone']
    storemanager = storeParams['storemanager']

    aux_store = Store(address, comercial_logo, name, phone, storemanager)
    db.session.add(aux_store)
    db.session.commit()
    return jsonify('OK'), 201

@blueprint_store.route('/store/<int:id>', methods=['PUT'])
@cross_origin()
def updateStore(id):
    try:
        storeParams = request.get_json()
        store = Store.query.get(id)

        if (storeParams.get('address')):
            store.address = storeParams['address']
        if (storeParams.get('comercial_logo')):
            store.product_img = storeParams['comercial_logo']
        if (storeParams.get('name')):
            store.name = storeParams['name']
        if (storeParams.get('phone')):
            store.phone = storeParams['phone']
        if (storeParams.get('storemanager')):
            store.storemanager = storeParams['storemanager']

        log_db = db.session.commit()

        return jsonify('OK'), 201

    except log_db as error:
        return error, 500

@blueprint_store.route('/store/<int:id>', methods=['DELETE'])
def deleteStore(id):
    try:
        store = Store.query.get(id)
        db.session.delete(store)
        db.session.commit()
        return jsonify('OK'), 201

    except:
        return 'Something went wrong', 500


@blueprint_store.route('/store/uploadImg', methods=['POST'])
@cross_origin()
def upload_file():
    print('Hi')
    print(request.files)
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('Hii')
            flash('No file part')
            return "Bad Usage", 401
        file = request.files['file']
        print('File here')
        print(file)
        imgName = file.filename.split('.')[0]
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        #f = open("../" + filename, "wb")
        #f.close()
        print(request.form)
        id = request.form.get('id')

        store = Store.query.get(id)

        pathToSave = "../src/storeImages/"
        urlToSave = "http://localhost:3000/api/v1/store/get_image/"
        filename = str(store.id) + "_store"

        #Save the url src in DB
        store.comercial_logo= urlToSave + filename
        print( urlToSave + filename )
        print(store.comercial_logo)
        print(store)
        print(db)
        log_db = db.session.commit()

        rute = os.path.dirname(__file__)
        file.save(os.path.join(rute , pathToSave + filename))



        return jsonify("OK"), 200
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@blueprint_store.route('/store/get_image/<string:img>')
def get_image(img):
   try:
    imgName = img.split('.')[0]
    rute = os.path.dirname(__file__)
    filename = (os.path.join(rute, '../src/storeImages/' + imgName))

    return send_file(filename, mimetype='image/jpeg')

   except:
        return jsonify("No image found"), 500
