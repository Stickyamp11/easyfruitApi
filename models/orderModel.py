from utils.db import db
from sqlalchemy import ForeignKey
import datetime as dt

class Orden(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        order_date = db.Column(db.Date)
        estimated_total = db.Column(db.Integer)
        status = db.Column(db.String(100))
        anotations = db.Column(db.String(100))
        times_ordered = db.Column(db.Integer())
        fCustomer = db.Column(db.Integer)
        fStore = db.Column(db.Integer)

        def __init__(self, order_date, estimated_total, status, anotations, times_ordered, fCustomer, fStore):
            self.order_date = order_date,
            self.estimated_total = estimated_total,
            self.status = status,
            self.fCustomer = fCustomer,
            self.fStore = fStore,
            self.anotations = anotations,
            self.times_ordered = times_ordered

        def to_dict(self):
            print(self.order_date)
            return {'id': self.id, 'order_date': str(self.order_date), 'estimated_total': self.estimated_total, 'status': self.status, 'anotations': self.anotations, 'times_ordered': self.times_ordered, 'fCustomer': self.fCustomer,
                    'fStore': self.fStore}


#class ProductSchema(ma.Schema):
            # class Meta:
#     fields = ('id', 'name', 'product_img', 'price_per_kg', 'fCategory')

#product_schema = ProductSchema()
#products_schema = ProductSchema(many=True)


