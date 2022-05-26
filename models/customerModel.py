from utils.db import db
from sqlalchemy import ForeignKey
class Customer(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(70))
        email = db.Column(db.String(70))
        phone = db.Column(db.String(70))
        passwd = db.Column(db.String(300))
        zip = db.Column(db.String(20))
        address = db.Column(db.String(500))
        seller = db.Column(db.String(2))


        def __init__(self, name, email, phone, passw, zip, address, seller):
            self.name = name,
            self.email = email,
            self.phone = phone,
            self.passwd = passw,
            self.zip = zip,
            self.seller = seller,
            self.address = address

        def to_dict(self):
            return {'id': self.id, 'name': self.name, 'email': self.email, 'phone': self.phone,
                    'passwd': self.passwd, 'zip': self.zip, 'address': self.address, 'seller': self.seller}


#class ProductSchema(ma.Schema):
            # class Meta:
#     fields = ('id', 'name', 'product_img', 'price_per_kg', 'fCategory')

#product_schema = ProductSchema()
#products_schema = ProductSchema(many=True)


