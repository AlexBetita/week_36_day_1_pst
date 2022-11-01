from flask import Blueprint, render_template
from ..models import Order

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def index():
	order = Order.query.all()
	print(order[0].shipped_date)
	return render_template("index.html")
