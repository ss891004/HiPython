from flask import Blueprint
from .models import Article

article_bp= Blueprint('bp_article',__name__,template_folder='templates')