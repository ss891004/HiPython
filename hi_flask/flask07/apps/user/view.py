

from flask import Blueprint, render_template,request,redirect,url_for
from .models import User

# 对单张表的CRUD, 模版的路径以当前文件的位置为准
user_bp = Blueprint('bp_user', __name__, template_folder='templates')

@user_bp.route("/")
def test():
    return "ok"
