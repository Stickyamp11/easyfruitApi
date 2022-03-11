from utils.db import db
from sqlalchemy.orm import relationship
class ProductCategory(db.Model):
       # __tablename__ = "productcategory"
      #  __table_args__ = {"schema": "public"}
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(70))
        #foreign key
        #products = relationship("Product")

        def __init__(self, name, product_img, price_per_kg, fcategory):
            self.name = name,


        def to_dict(self):
            return {'id': self.id, 'name': self.name}


#class ProductSchema(ma.Schema):
            # class Meta:
#     fields = ('id', 'name', 'product_img', 'price_per_kg', 'fCategory')

#product_schema = ProductSchema()
#products_schema = ProductSchema(many=True)


