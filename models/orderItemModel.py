from utils.db import db
from sqlalchemy import ForeignKey
class Ordenitem(db.Model):
        ordenId = db.Column(db.Integer, primary_key=True )
        productId = db.Column(db.Integer, primary_key=True)
        methodSelected = db.Column(db.String(70))
        unitsToBuy = db.Column(db.String(70))
        estimated_price = db.Column(db.String(70))
        def __init__(self, ordenId, productId, methodSelected, unitsToBuy, estimated_price):
            self.ordenId = ordenId,
            self.productId = productId,
            self.methodSelected = methodSelected,
            self.unitsToBuy = unitsToBuy,
            self.estimated_price = estimated_price


        def to_dict(self):
            return {'ordenId': self.ordenId, 'productId': self.productId,
                    'methodSelected': self.methodSelected, 'unitsToBuy': self.unitsToBuy, 'estimated_price': self.estimated_price}


#class ProductSchema(ma.Schema):
            # class Meta:
#     fields = ('id', 'name', 'product_img', 'price_per_kg', 'fCategory')

#product_schema = ProductSchema()
#products_schema = ProductSchema(many=True)


