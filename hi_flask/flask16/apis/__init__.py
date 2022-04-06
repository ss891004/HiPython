
from flask_restx import Api

from .hw01 import HelloWorld
from .hw02 import ns as hw02_ns
from .hw03 import ns as hw03_ns

'''
当引入本模块时，从上到下，全部执行，主程序中，再执行init_api 函数
'''
# 实例化一个 Api 对象
api =Api(ordered=True)
# 注册命名空间
api.add_namespace(hw02_ns)
# 注册资源，此时该资源属于默认命名空间
api.add_resource(HelloWorld,'/b', endpoint='xxxy')

api.add_namespace(hw03_ns)
# 将api 注册到 app 上
def init_api(app):
    api.init_app(app, version='1.0', title='flask rest',description='a spec flask rest',)

