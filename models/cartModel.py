from utils.db import db
from sqlalchemy import ForeignKey
class Cart(db.Model):
        customerId = db.Column(db.Integer, primary_key=True)
        productId = db.Column(db.Integer, primary_key=True)

        def __init__(self, customerId, productId):
            self.customerId = customerId,
            self.productId = productId,


        def to_dict(self):
            return {'customerId': self.customerId, 'productId': self.productId}

