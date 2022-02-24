from asyncio.windows_events import NULL
from flask import Flask, jsonify, request, render_template, Response
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'easyfruit'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def Index():
    return 'Hola mundo'


@app.route('/customer',methods=['GET'])
def getAllUsers():
        cur = mysql.connection.cursor()
        cur.execute('Select * from customer')
        data = cur.fetchall()
        customer_array = []
        for row in data:
            customer_array.append({'id': row[0], 'name': row[1], 'email': row[2], 'phone': row[3], 'pass': row[4]})

        return jsonify(customer_array), 200

@app.route('/customer/<int:id>', methods=['GET'])
def getUser(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('Select * from customer where id = ' + str(id))
        data = cur.fetchone()
        return jsonify({'id': str(data[0]), 'name': str(data[1]), 'email': str(data[2]), 
        'phone': str(data[3]), 'pass': str(data[4])}), 201
    except:
        return 'Something went wrong', 500

@app.route('/customer', methods=['POST'])
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

@app.route('/customer/<int:id>', methods=['PUT'])
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

@app.route('/customer/<int:id>', methods=['DELETE'])
def deleteUser(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('delete from customer where id = ' + str(id))
        cur.connection.commit()        
        return jsonify('OK'), 201
    except:
        return 'Something went wrong', 500


if __name__ == '__main__':
    app.run(port = 3000, debug = True)