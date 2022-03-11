from utils.db import db
from sqlalchemy import ForeignKey
class storeManager(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(70))
        email = db.Column(db.String(70))
        phone = db.Column(db.String(70))
        passw = db.Column(db.String(300))

        def __init__(self, name, email, phone, passw):
            self.name = name,
            self.email = email,
            self.phone = phone,
            self.passw = passw

        def to_dict(self):
            return {'id': self.id, 'name': self.name, 'email': self.email, 'phone': self.phone,
                    'passw': self.passw}


#class ProductSchema(ma.Schema):
            # class Meta:
#     fields = ('id', 'name', 'product_img', 'price_per_kg', 'fCategory')

#product_schema = ProductSchema()
#products_schema = ProductSchema(many=True)


