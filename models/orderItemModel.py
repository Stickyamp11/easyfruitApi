from utils.db import db
from sqlalchemy import ForeignKey
class OrdenItem(db.Model):
        ordenId = db.Column(db.Integer,ForeignKey('orden.id'), primary_key=True )
        productId = db.Column(db.Integer, ForeignKey('product.id'), primary_key=True)

        def __init__(self, ordenId, productId):
            self.ordenId = ordenId,
            self.productId = productId,


        def to_dict(self):
            return {'id': self.id, 'ordenId': self.ordenId, 'productId': self.productId}


#class ProductSchema(ma.Schema):
            # class Meta:
#     fields = ('id', 'name', 'product_img', 'price_per_kg', 'fCategory')

#product_schema = ProductSchema()
#products_schema = ProductSchema(many=True)


