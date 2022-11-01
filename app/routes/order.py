from flask import BluePrint, renderTemplate

order_bp = BluePrint('order', __name__, url_prefix='orders')