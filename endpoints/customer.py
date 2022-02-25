from asyncio.windows_events import NULL
from flask import Flask, jsonify, request, render_template, Response,Blueprint
from flask_mysqldb import MySQL
from app import mysql

# imports required to work properly
# define the blueprint

blueprint_customer = Blueprint(name="blueprint_customer", import_name=__name__)

@blueprint_customer.route('/customer',methods=['GET'])
def getAllUsers():
        cur = mysql.connection.cursor()
        cur.execute('Select * from customer')
        data = cur.fetchall()
        customer_array = []
        for row in data:
            customer_array.append({'id': row[0], 'name': row[1], 'email': row[2], 'phone': row[3], 'pass': row[4]})

        return jsonify(customer_array), 200

@blueprint_customer.route('/customer/<int:id>', methods=['GET'])
def getUser(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('Select * from customer where id = ' + str(id))
        data = cur.fetchone()
        return jsonify({'id': str(data[0]), 'name': str(data[1]), 'email': str(data[2]), 
        'phone': str(data[3]), 'pass': str(data[4])}), 201
    except:
        return 'Something went wrong', 500

@blueprint_customer.route('/customer', methods=['POST'])
def createUser():
    userParams = request.get_json()
    name = userParams['name']
    email = userParams['email']
    phone = userParams['phone']
    passw = userParams['pass']    
    cur = mysql.connection.cursor()
    cur.execute('insert into customer (name,email,phone,pass) values (%s,%s,%s,%s)', (name,email,phone,passw))
    cur.connection.commit()
    return jsonify('OK'), 201

@blueprint_customer.route('/customer/<int:id>', methods=['PUT'])
def updateUser(id):
    userParams = request.get_json()
    name = userParams['name']
    email = userParams['email']
    phone = userParams['phone']
    passw = userParams['pass']    
    cur = mysql.connection.cursor()
    cur.execute('update customer set name=%s,email=%s,phone=%s,pass=%s where id=%s', (name,email,phone,passw,id))
    cur.connection.commit()
    return jsonify('OK'), 201

@blueprint_customer.route('/customer/<int:id>', methods=['DELETE'])
def deleteUser(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('delete from customer where id = ' + str(id))
        cur.connection.commit()        
        return jsonify('OK'), 201
    except:
        return 'Something went wrong', 500
