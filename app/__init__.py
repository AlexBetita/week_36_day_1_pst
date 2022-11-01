from flask import Flask
from .config import Configuration
<<<<<<< HEAD
from .routes import main_bp
from .routes import order_bp
=======
from .routes import main_bp, customer_bp
>>>>>>> 52152235bf12d12cb1336e56548e050e6313590b
from .models import db, Customer, Order

# this line of code is just for an example
# from .models import Customer, session

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(main_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(order_bp)
db.init_app(app)


# # this line of code is just for an example
with app.app_context():
	from datetime import datetime
	db.drop_all()
	db.create_all()
	customer1 = Customer(customer_name='Alex', last_name='Betita', first_name='Alex', phone=12345)
	session.add(customer1)
	session.commit()
	print(customer1.id)

	db.session.add(customer1)
	db.session.commit()

	order1 = Order(order_date=datetime.now(), shipped_date=datetime.now(),
				   status=True, comments='Expensive', customer_id=customer1.id)
	print(customer1.id)
	db.session.add(order1)
	db.session.commit()

	customer2 = Customer(customer_name='Karen', last_name='Huang', first_name='Karen', phone=6789)
	session.add(customer2)
	session.commit()
	print(customer2.id)

	db.session.add(customer2)
	db.session.commit()

	customer3 = Customer(customer_name='George', last_name='Merida', first_name='George', phone=101112)
	session.add(customer3)
	session.commit()
	print(customer3.id)

	db.session.add(customer3)
	db.session.commit()

	customer4 = Customer(customer_name='Kelly', last_name='Artola', first_name='Kelly', phone=14151617)
	session.add(customer4)
	session.commit()
	print(customer4.id)

	db.session.add(customer4)
	db.session.commit()

	customer5 = Customer(customer_name='Alonso', last_name='Vazquez', first_name='Alonso', phone=181920)
	session.add(customer5)
	session.commit()
	print(customer5.id)

	db.session.add(customer5)
	db.session.commit()

	order2 = Order(order_date=datetime.now(), shipped_date=datetime.now(),
				   status=True, comments='pearls', customer_id=customer2.id)
	print(customer2.id)
	db.session.add(order2)
	db.session.commit()

	order3 = Order(order_date=datetime.now(), shipped_date=datetime.now(),
				   status=True, comments='Manhattan sunglasses', customer_id=customer3.id)
	print(customer3.id)
	db.session.add(order3)
	db.session.commit()

	order4 = Order(order_date=datetime.now(), shipped_date=datetime.now(),
				   status=True, comments='boots', customer_id=customer4.id)
	print(customer4.id)
	db.session.add(order4)
	db.session.commit()

	order5 = Order(order_date=datetime.now(), shipped_date=datetime.now(),
				   status=True, comments='pink diamonds', customer_id=customer5.id)
	print(customer5.id)
	db.session.add(order5)
	db.session.commit()
