from utils.db import db
from sqlalchemy import ForeignKey
class Store(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        address = db.Column(db.String(90))
        comercial_logo = db.Column(db.String(300))
        name = db.Column(db.String(60))
        phone = db.Column(db.String(60))
        storemanager = db.Column(db.String(200))

        def __init__(self, address, comercial_logo, name, phone, storemanager):
            self.address = address,
            self.comercial_logo = comercial_logo,
            self.name = name,
            self.phone = phone,
            self.storemanager = storemanager

        def to_dict(self):
            return {'id': self.id, 'address': self.address, 'comercial_logo': self.comercial_logo, 'name': self.name, 'phone': self.phone , 'storemanager': self.storemanager}


#class ProductSchema(ma.Schema):
            # class Meta:
#     fields = ('id', 'name', 'product_img', 'price_per_kg', 'fCategory')

#product_schema = ProductSchema()
#products_schema = ProductSchema(many=True)


