from flask import Flask
from .ext import init_ext
from apis import init_api


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI']="mysql+mysqlconnector://root:123456@127.0.0.1:3306/hi_flask2"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_ext(app)
    init_api(app)

    return app