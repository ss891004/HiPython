

from flask import Blueprint, render_template,request,redirect,url_for
from .models import User

# 对单张表的CRUD, 模版的路径以当前文件的位置为准
user_bp = Blueprint('bp_user', __name__, template_folder='tmp_user')


@user_bp.route('/')
def index():
    # 查询当前所有的用户
    users=User.query.all()
    return render_template('index.html', us=users)


# 注册
@user_bp.route('/register',methods=['POST', 'GET'])
def index3():
    if request.method == 'POST':
        print(request.form['u_name'])
        print(request.form['u_pass'])
        print(request.form['u_phone'])

        u = User() # 实力化一个新的对象
        u.username=request.form['u_name'] 
        u.password=request.form['u_pass']
        u.phone=request.form['u_phone']
        u.save()

        # 转发到首页，查询出当前的所有用户
        # url_for 反向解析
        return redirect(url_for('bp_user.index')) # 蓝本的名称+函数的名称，不是路由中的名称

    # get请求，首次访问，直接返回页面
    return render_template('register.html')



@user_bp.route('/r_login')
def login():
    if request.method=="POST":
        print(request.form['l_name'])
        print(request.form['l_pass'])

        # 根据用户名查询数据库中密码

        # 比较密码

        # 个人中心
        return render_template('center_info.html')

    return render_template('login.html')


# 退出
@user_bp.route('/r_logout')
def logout():
    # cookie 和 session 的处理
    return render_template('login.html')

@user_bp.route('/r_update/<int:id>',methods=['POST', 'GET'])
def update_i(id):
    if request.method=="POST":
        u =  User.query.filter_by(id=id).first()
        u.username=request.form['i_name'] 
        u.password=request.form['i_pass']
        u.phone=request.form['i_phone']
        u.update()
        return redirect(url_for('bp_user.index'))  # 重定向

    u =  User.query.filter_by(id=id).first()
    return render_template('update_info.html',u=u)

@user_bp.route('/r_delete/<int:id>')
def delete_i(id):
    u =  User.query.filter_by(id=id).first() # 不能 u=User() , 需要重数据库中查询出实体对象
    u.delete()
    return redirect(url_for('bp_user.index'))