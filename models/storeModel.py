from utils.db import db
from sqlalchemy import ForeignKey
class Store(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        address = db.Column(db.String(90))
        comercial_logo = db.Column(db.String(300))
        name = db.Column(db.String(60))

        def __init__(self, address, comercial_logo, name):
            self.address = address,
            self.comercial_logo = comercial_logo,
            self.name = name

        def to_dict(self):
            return {'id': self.id, 'address': self.address, 'comercial_logo': self.comercial_logo, 'name': self.name}


#class ProductSchema(ma.Schema):
            # class Meta:
#     fields = ('id', 'name', 'product_img', 'price_per_kg', 'fCategory')

#product_schema = ProductSchema()
#products_schema = ProductSchema(many=True)


