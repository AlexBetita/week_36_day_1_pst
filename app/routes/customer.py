from flask import Blueprint, render_template

customer_bp = Blueprint('customer', __name__, url_prefix='/customers')

@customer_bp.route("/")
def index():
	return render_template("index.html", customers = customers)
