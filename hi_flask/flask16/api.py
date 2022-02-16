from flask import Flask,Blueprint
from flask_restx import Resource, Api, Namespace,fields
app = Flask(__name__)

api =Api()
api.init_app(app, version='2.0', title='flask rest',description='A simple demo',)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'hello': 'world'}

# 注册资源
api.add_resource(HelloWorld, '/hw')


# 指定具体的命名空间
ns = Namespace('Todo_API', description='Todo_API')

model = ns.model('Model', {
    'task': fields.String,
    'xxx': fields.String,
    'yyyy':fields.String,
    #'uri': fields.Url('todo_ep')
})

@ns.route('/aaaa')
class Todo(Resource):
    @ns.marshal_with(model)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')

api.add_namespace(ns,path='/hw2')

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
    print(app.url_map)
    print(api)
    app.run(debug=True)