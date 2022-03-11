from utils.db import db
from sqlalchemy import ForeignKey
class Orden(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        order_date = db.Column(db.Date)
        estimated_total = db.Column(db.Integer)
        fCustomer = db.Column(db.Integer, ForeignKey('customer.id'))
        fStore = db.Column(db.Integer, ForeignKey('store.id'))

        def __init__(self, order_date, estimated_total, fCustomer, fStore):
            self.order_date = order_date,
            self.estimated_total = estimated_total,
            self.fCustomer = fCustomer,
            self.fStore = fStore

        def to_dict(self):
            return {'id': self.id, 'order_date': self.order_date, 'estimated_total': self.estimated_total, 'fCustomer': self.fCustomer,
                    'fStore': self.fStore}


#class ProductSchema(ma.Schema):
            # class Meta:
#     fields = ('id', 'name', 'product_img', 'price_per_kg', 'fCategory')

#product_schema = ProductSchema()
#products_schema = ProductSchema(many=True)


