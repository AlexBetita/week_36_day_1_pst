from flask import BluePrint, renderTemplate
from .models import orders

order_bp = BluePrint('order', __name__, url_prefix='/orders')

@order_bp.route("/")
def all_orders():
    order = orders.query.all()
    print(order)
    return renderTemplate('order.html', order=order)