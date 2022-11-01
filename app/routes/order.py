from flask import BluePrint, renderTemplate
from .models import order

order_bp = BluePrint('order', __name__, url_prefix='orders')

@order_bp.route("/")
def all_orders():
    order = Order.query.all()
    return renderTemplate('order.html', order=order)