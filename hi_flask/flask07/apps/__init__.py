from .user.view import user_bp
from .article.views import article_bp
def  init_view(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(article_bp)
