
from flask_restx import Api

from apps.apis.news_api import ns as news_ns

'''
当引入本模块时，从上到下，全部执行，主程序中，再执行init_api 函数
'''
# 实例化一个 Api 对象
api =Api(ordered=True)
# 注册命名空间

api.add_namespace(news_ns)
# 将api 注册到 app 上
def init_api(app):
    api.init_app(app, version='1.0', title='flask rest',description='a spec flask rest',)

