

from flask import Blueprint, render_template,request,redirect,url_for
from .models import Comment,Article

comment_bp = Blueprint('bp_comment', __name__,template_folder='../templates')

# 通过文章，找评论
@comment_bp.route("/get_com_art/<int:id>")
def get_comment_by_article(id):


    u =  Article.query.filter_by(id=id).first() 

    print(u.comments)
    print(u.br_xy)

    return render_template('get_com_art.html',u=u)

# 通过评论，找文章
@comment_bp.route("/get_art_com")
def get_article_by_comment():
    pass