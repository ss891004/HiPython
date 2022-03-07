

from flask import Blueprint, render_template
from .models import User

user_bp = Blueprint('user', __name__,template_folder='templates')


@user_bp.route('/')
def index():

    # 查询当前所有的用户
    users=User.query.all()

    return render_template('index.html', us=users)

@user_bp.route('/hi')
def index2():
     return render_template('index.html', msg="这天气适合睡觉")


# 注册
@user_bp.route('/register')
def index3():
    pass
