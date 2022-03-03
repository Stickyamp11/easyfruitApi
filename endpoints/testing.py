from asyncio.windows_events import NULL
from flask import Flask, jsonify, request, render_template, Response,Blueprint
from flask_mysqldb import MySQL
from http import HTTPStatus
import app
import os
#import requests




def upload():
    file = request.files['file']
    file.save(os.path.join(app.config['productImages'], 'id_product.png'))
instances = 'wfeofm'
with open(instances + '_product.png', 'wb') as f:
    f.write('something')


# id_product



