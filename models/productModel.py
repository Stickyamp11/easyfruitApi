from utils.db import db
from sqlalchemy import ForeignKey
class Product(db.Model):
        __tablename__ = "product"
       # __table_args__ = {"schema": "public"}
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(70))
        product_img = db.Column(db.String(70))
        price_per_kg = db.Column(db.String(70))
        price_per_unit = db.Column(db.String(70))
        price_per_pack = db.Column(db.String(70))
        packQuantity = db.Column(db.String(70))
        description = db.Column(db.String(5000))
        methodsAllowed = db.Column(db.String(70))
        fCategory = db.Column(db.Integer) #, ForeignKey('productcategory.id'))
        fStore = db.Column(db.Integer) # ForeignKey for store.id

        def __init__(self, name, product_img, price_per_kg, price_per_unit, price_per_pack, packQuantity, fcategory, fStore, description, methodsAllowed):
            self.name = name,
            self.product_img = product_img,
            self.price_per_kg = price_per_kg,
            self.price_per_unit = price_per_unit,
            self.price_per_pack = price_per_pack
            self.packQuantity = packQuantity,
            self.fCategory = fcategory,
            self.fStore = fStore,
            self.description = description,
            self.methodsAllowed = methodsAllowed

        def to_dict(self):
            return {'id': self.id, 'name': self.name, 'product_img': self.product_img, 'price_per_kg': self.price_per_kg, 'price_per_unit': self.price_per_unit, 'price_per_pack': self.price_per_pack,'packQuantity': self.packQuantity,
                    'fCategory': self.fCategory, 'fStore': self.fStore, 'description': self.description, 'methodsAllowed': self.methodsAllowed}


#class ProductSchema(ma.Schema):
            # class Meta:
#     fields = ('id', 'name', 'product_img', 'price_per_kg', 'fCategory')

#product_schema = ProductSchema()
#products_schema = ProductSchema(many=True)


