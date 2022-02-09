from flask import Blueprint

user_bp = Blueprint('user', __name__,template_folder='../templates')


@user_bp.route("/index")
def index():
    return "user-index"