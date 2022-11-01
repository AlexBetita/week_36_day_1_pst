# declarative mapping

# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.schema import Column
# from sqlalchemy.types import Integer, String

# # base class that contains methods and functions that allow us to query, filter, search and etc.
# Base = declarative_base()

# class Customer(Base):

# 	__tablename__ = 'customers'


# 	id = Column(Integer, primary_key=True, autoincrement=True)
# 	customer_name = Column(String)
# 	last_name = Column(String)
# 	first_name = Column(String)
# 	phone = Column(Integer)

from .db import db

class Customer(db.Model):

	__tablename__ = 'customers'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	customer_name = db.Column(db.String)
	last_name = db.Column(db.String)
	first_name = db.Column(db.String)
	phone = db.Column(db.Integer)

	# orders = db.relationship('Order', backref='customers')
