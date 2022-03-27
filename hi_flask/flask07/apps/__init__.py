from .article.v_user import user_bp
from .article.v_article import article_bp
from .article.v_comment import comment_bp

def  init_view(app):
    print(app)
    app.register_blueprint(user_bp)
    app.register_blueprint(article_bp)
    app.register_blueprint(comment_bp)
