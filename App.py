from asyncio.windows_events import NULL
from flask import Flask, jsonify, request, render_template, Response
from flask_mysqldb import MySQL
#from flasgger import swag_from
from http import HTTPStatus




#def __init__():


#def create_app():

    # init Flask app
app = Flask(__name__)

app.config['SWAGGER'] = {
    'title': 'EasyFruit API',
    }
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'easyfruit'
    #app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
    #swagger = Swagger(app)

app.config.from_pyfile('config.py')
    
    #return app




if __name__ == '__main__':
   
    #app = create_app()
    
    # load modules
    from endpoints.customer import blueprint_customer
    # register blueprints. ensure that all paths are versioned!
    app.register_blueprint(blueprint_customer, url_prefix='/api/v1')
    
    app.run( port=3000, debug= True)