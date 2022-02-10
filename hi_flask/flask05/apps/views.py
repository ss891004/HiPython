from flask import Blueprint, render_template

from exts.ext import dbs

from .models import User


# 模版文件在当前目录的template 中
first = Blueprint('first', __name__,template_folder='template')


@first.route('/index/')
def index():
    # return '我是蓝图的主页'
    return render_template('index2.html', msg="这天气适合睡觉")


@first.route('/createdb/')
def createdb():
    dbs.create_all()
    return '创建成功'


@first.route('/dropdb/')
def dropdb():
    dbs.drop_all()
    return '删除成功'


@first.route('/adduser/')
def add_user():
    user = User()
    user.username = "Tom"
    user.phone="15250630870"
    user.password="Tommmmm"
    user.sex='1'

    dbs.session.add(user)
    dbs.session.commit()

    return '创建成功'

@first.route('/getuser/')
def get_user():

    return '创建成功'




second = Blueprint('second', __name__)

@second.route('/hello/')
def hello():
    return 'Second Blue'


third = Blueprint('third', __name__)
@third.route('/hi/')
def hi():
    return 'Hi Thrid'