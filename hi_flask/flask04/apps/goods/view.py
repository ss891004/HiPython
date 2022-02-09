

from flask import Blueprint

goods_bp = Blueprint('goods', __name__,template_folder='../templates')


@goods_bp.route("/index")
def index():
    return "user-index"
