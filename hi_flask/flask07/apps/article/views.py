from flask import Blueprint,render_template
from .models import Article


article_bp= Blueprint('bp_article', __name__, template_folder='templates')


@article_bp.route("/")
def test():
    return render_template('add_article.html')


@article_bp.route("/add")
def add():
    return "ok"