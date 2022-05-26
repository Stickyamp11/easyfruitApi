from asyncio.windows_events import NULL
from flask import Flask, jsonify, request, render_template, Response, Blueprint
from flask_mysqldb import MySQL
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

import routes.customer
from models.customerModel import Customer
import jwt
from werkzeug.security import generate_password_hash,check_password_hash
import datetime
from functools import wraps
from http import HTTPStatus
from config import MYSQL_HOST
from flask_cors import cross_origin


#if __name__ == '__main__':

#def __init__():


#def create_app():

# init Flask app
app = Flask(__name__)
CORS(app)

##app.config['CORS_HEADERS'] = 'Content-Type, Authorization, Origin'
#cors = CORS(app, resources={r"*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/easyfruit'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "fijowqfmmfiornrrqowngrowngoqwggri,cpvr"
app.config['UPLOAD_FOLDER'] = '/src'

SQLALCHEMY_ENGINE_OPTIONS = {
    "max_overflow": 15,
    "pool_pre_ping": True,
    "pool_recycle": 600 * 600,
    "pool_size": 400,
    "pool_timeout": 5
}
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = SQLALCHEMY_ENGINE_OPTIONS
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



engine_container = db.get_engine(app)

#app = create_app()



@app.after_request
@cross_origin()
def cleanup(Response):
    """
    This method cleans up the session object and also closes the connection pool using the dispose method.
    """
    db.session.close()
    engine_container.dispose()

    #Original response here
    return Response;






# load modules
from routes.customer import blueprint_customer
from routes.store import blueprint_store
from routes.productCategory import blueprint_productCategory
from routes.product import blueprint_product
from routes.authentication import blueprint_authentication
from routes.cart import blueprint_cart
from routes.order import blueprint_order
from routes.orderItem import blueprint_orderitem
# register blueprints. ensure that all paths are versioned!
app.register_blueprint(blueprint_customer, url_prefix='/api/v1')
app.register_blueprint(blueprint_store, url_prefix='/api/v1')
app.register_blueprint(blueprint_productCategory, url_prefix='/api/v1')
app.register_blueprint(blueprint_product, url_prefix='/api/v1')
app.register_blueprint(blueprint_order, url_prefix='/api/v1')
app.register_blueprint(blueprint_orderitem, url_prefix='/api/v1')
app.register_blueprint(blueprint_authentication, url_prefix='/api/v1')
app.register_blueprint(blueprint_cart, url_prefix='/api/v1')
app.run( port=3000, debug= False)
