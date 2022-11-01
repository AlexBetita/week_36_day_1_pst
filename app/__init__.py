from flask import Flask
from .config import Configuration
from .routes import main_bp
from .models import db, Customer, Order

# this line of code is just for an example
# from .models import Customer, session

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(main_bp)
app.register_blueprint(order_bp)
db.init_app(app)


# # this line of code is just for an example
with app.app_context():
	from datetime import datetime
	db.drop_all()
	db.create_all()
	# customer1 = Customer(customer_name='Alex', last_name='Betita', first_name='Alex', phone=12345)
	# # session.add(customer1)
	# # session.commit()
	# print(customer1.id)

	# db.session.add(customer1)
	# db.session.commit()

	# order1 = Order(order_date=datetime.now(), shipped_date=datetime.now(),
	# 			   status=True, comments='Expensive', customer_id=customer1.id)
	# print(customer1.id)
	# db.session.add(order1)
	# db.session.commit()
