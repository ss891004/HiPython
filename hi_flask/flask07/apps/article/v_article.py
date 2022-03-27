from flask import Blueprint,render_template,request
from .models import Article
from .models import User


article_bp= Blueprint('bp_article', __name__,template_folder='../templates')


@article_bp.route("/")
def test():

    ## 获取当前所有的用户

    u_li= User.query.all()

    return render_template('add_article.html',us=u_li)


@article_bp.route("/add", methods=['POST','GET'])
def add():

    # 接收post请求过来的参数

    print(request.form['a_title'])
    print(request.form['a_context'])
    print(request.form['a_user'])

    art = Article()
    art.content=request.form['a_context']
    art.title=request.form['a_title']
    art.user_id=request.form['a_user']

    art.save()

    return "ok"

# 根据用户的id，查询其所有的文章信息
@article_bp.route("/getArt/<int:id>",methods=['POST','GET'])
def getArticleByUser(id):

    u =  User.query.filter_by(id=id).first() 

    return render_template('get_article.html',u=u)


# 根据文章的id，查询其用户的信息
# 通过 articles=dbs.relationship('Article',backref='br_user') 的 反应引用，获取 用户信息
@article_bp.route("/getUser/<int:id>",methods=['POST','GET'])
def getUserByArticle(id):

    u =  Article.query.filter_by(id=id).first() 

    return render_template('get_user.html',u=u)
