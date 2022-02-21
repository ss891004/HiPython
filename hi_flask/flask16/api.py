from flask import Flask,Blueprint
from flask_restx import Resource, Api, Namespace,fields

app = Flask(__name__)

# 作为flask的第三方插件， 实例化对象
api =Api()
# 和app判定关系
api.init_app(app, version='2.0', title='flask rest',description='A simple demo',)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'hello': 'world'}

# 注册资源
api.add_resource(HelloWorld, '/hw')
#==============================================================================
# 指定具体的命名空间
ns = Namespace('Todo_API', description='Todo_API')

text_req = ns.model('text_msg', {
    'agentid': fields.String,
    'to_user': fields.String,
    'text_context':fields.String,
    'template_id': fields.String
})

#text_resp = ns.model('text_resp', {'name': fields.String})

@ns.route('/do')
class Todo(Resource):
    @ns.marshal_with(text_req)
    #@ns.expect(text_resp)
    def get(self, **kwargs):
        return kwargs

api.add_namespace(ns,path='/hw2')

#==============================================================================
hw_bp = Blueprint('hw3', __name__)

class User(Resource):
    def get(self):
        return   {"msg":"user------get"}

    def post(self):
        return {"msg":"user----post"}

    def put(self):
        return {"msg":"user----put"}

    def delete(self):
        return {"msg":"user------delete"}

api.add_resource(User,"/hw3")

# 默认的命名空间
@api.route('/hello')
class HelloWorld1(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True)