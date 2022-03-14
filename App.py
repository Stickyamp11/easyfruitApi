from asyncio.windows_events import NULL
from flask import Flask, jsonify, request, render_template, Response
from flask_mysqldb import MySQL
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#from flasgger import swag_from
from http import HTTPStatus
from config import MYSQL_HOST



#if __name__ == '__main__':

#def __init__():


#def create_app():

    # init Flask app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/easyfruit'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)


db = SQLAlchemy(app)
ma = Marshmallow(app)
app.config['SWAGGER'] = {
    'title': 'EasyFruit API',
    }

    #app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

    #swagger = Swagger(app)

app.config.from_object('config')
print(os.environ.get('MYSQL_HOST'))
    #return app





#app = create_app()

# load modules
from routes.customer import blueprint_customer
from routes.store import blueprint_store
#from routes.productCategory import blueprint_productCategory
from routes.product import blueprint_product
#from routes.order import blueprint_order
# register blueprints. ensure that all paths are versioned!
app.register_blueprint(blueprint_customer, url_prefix='/api/v1')
app.register_blueprint(blueprint_store, url_prefix='/api/v1')
#app.register_blueprint(blueprint_productCategory, url_prefix='/api/v1')
app.register_blueprint(blueprint_product, url_prefix='/api/v1')
#app.register_blueprint(blueprint_order, url_prefix='/api/v1')
app.run( port=3000, debug= True)