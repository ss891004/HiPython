
from flask_restx import Namespace,fields,Resource,reqparse

from models.user import User

# 命名空间+ 类视图
ns = Namespace('hw02', description='xxxxx')

# 路由
# 请求参数
# 常见的请求
@ns.route('/mm/<string:sid>/<int:iid>')
class Message(Resource):
    def get(self, sid,iid): # 参数名字必须和路由中的一样
        return "hello Message get " + sid + str(iid)
    def post(self ,sid,iid):
        return "hello Mesage post "
    def put(self,sid,iid):
        return "hello Message put "
    def delete(self,sid,iid):
        return "hello Message delete"



