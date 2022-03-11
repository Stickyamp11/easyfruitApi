from utils.db import db
from sqlalchemy import ForeignKey
class Product(db.Model):
       # __tablename__ = "product"
       # __table_args__ = {"schema": "public"}
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(70))
        product_img = db.Column(db.String(70))
        price_per_kg = db.Column(db.String(70))
        fCategory = db.Column(db.Integer) #, ForeignKey('productcategory.id'))

        def __init__(self, name, product_img, price_per_kg, fcategory):
            self.name = name,
            self.product_img = product_img,
            self.price_per_kg = price_per_kg,
            self.fCategory = fcategory

        def to_dict(self):
            return {'id': self.id, 'name': self.name, 'product_img': self.product_img, 'price_per_kg': self.price_per_kg,
                    'fCategory': self.fCategory}


#class ProductSchema(ma.Schema):
            # class Meta:
#     fields = ('id', 'name', 'product_img', 'price_per_kg', 'fCategory')

#product_schema = ProductSchema()
#products_schema = ProductSchema(many=True)


