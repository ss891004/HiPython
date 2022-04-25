from flask import Flask
from exts.ext import init_ext
from apps.apis import init_api

from apps.models.news_model import NewsModel


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI']="mysql+mysqlconnector://root:123456@127.0.0.1:3306/flask16"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_ext(app)
    init_api(app)

    print(app.url_map)
    return app