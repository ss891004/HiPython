

from flask import Blueprint, render_template
from .models import User

user_bp = Blueprint('user', __name__,template_folder='templates')


@user_bp.route('/')
def index():
    return 'hello ~~~'

@user_bp.route('/hi')
def index2():
     return render_template('index.html', msg="这天气适合睡觉")
