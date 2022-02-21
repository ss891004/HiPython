
from flask_restx import Namespace,fields,Resource,reqparse

from models.user import User

# 命名空间+ 类视图
ns = Namespace('msg', description='hi message')

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


reps_user = {
    'id':fields.String,
    'username':fields.String,
    'password':fields.String,
    'insert_time' : fields.DateTime,
    'tel_phone': fields.String
}

# 必须注册到命名空间中
resp_u= ns.model('resp_u',reps_user)


# 数据的查询，增加
@ns.route('/mn/<string:sid>')
class Message2(Resource):
    @ns.marshal_with(resp_u)
    def get(self,sid):
        return User.query.all()

    def post(self,sid):

        user = User()
        user.username='aaa'
        user.password='bb'
        user.sex='m'
        user.phone=sid
        user.save()

        pass


# 参数解析
# parser = reqparse.RequestParser() # 解析对象
parser = ns.parser()
parser.add_argument('p_1',location=['form']) # 添加参数
parser.add_argument('p_2', location=['form']) # 添加参数

@ns.route('/mp')
class Message3(Resource):

    # http://127.0.0.1:5000/a/mp?p_1=222&P_2=33333
    # get 请求的参数 在postman中 params
    def get(self):
        args = parser.parse_args()
        print(args)
        return "args"

    # post 请求在 body 中， params中的参数也可以获取，所以需要增加 location 
    # 如何添加 expect ??
    def post(self):
        args = parser.parse_args()
        print(args)
        return "args"

