from flask import Flask

from One import init_view

from Two import init_two

from .ext import init_ext

from .setting import envs

from Apis import init_api

def create_app():
    app = Flask(__name__)

    # 加载settings中的配置
    app.config.from_object(envs.get('develop'))

    # 加载扩展库
    init_ext(app)

    # 加载路由
    init_view(app)
    init_two(app)

    init_api(app)
    return app