
from flask_restx import Namespace,fields,Resource,reqparse
from werkzeug.datastructures import FileStorage
from models.user import User


ns = Namespace('hw03', description='hi message')


# 参数解析
parser1 = reqparse.RequestParser() # 解析对象
parser1.add_argument('p_1',type=str,location='args') # 添加参数
parser1.add_argument('p_2', type=int) # 添加参数

reps_user1 = {
    'id':fields.String,
    'username':fields.String,
    'password':fields.String,
    'sex':fields.String,
    'insert_time' : fields.DateTime,
    'phone': fields.String
}

r_parser = ns.model('xxxxx',reps_user1)

@ns.route('/h03')
class HelloWorld03(Resource):

    # http://127.0.0.1:5000/a/mp?p_1=222&P_2=33333
    # get 请求的参数 在postman中 params
    @ns.expect(parser1)
    def get(self):
        args = parser1.parse_args()
        print(args)
        return  'xxx'

    # post 请求在 body 中， params中的参数也可以获取，所以需要增加 location 
    @ns.marshal_with(r_parser) # 输出的对象格式
    @ns.expect(parser1)  # 输入的参数格式
    def post(self):
        args = parser1.parse_args()
        id=args['p_2']
        u= User.query.filter_by(id=id).first()

        # 多条记录
        return u

    @ns.doc(responses={403: 'Not Authorized'})
    def delete(self):
        ns.abort(403)


# 参数解析
parser2 = reqparse.RequestParser() # 解析对象
parser2.add_argument('file', location='files', type=FileStorage, required=True) # File Upload

@ns.route('/h04')
class HelloWorld04(Resource):

    @ns.expect(parser2)
    def post(self):
        args = parser2.parse_args()
        uploaded_file = args['file']
        print(uploaded_file)

