from flask_restx import Resource
from models.user import User
import random

# 入门示例

# 类视图  CBV（class base views）
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):

        u = User()
        u.age=11
        u.username='1'
        u.password='1'
        u.sex='男'
        u.phone='138'+str(random.randint(10000000, 90000000))
        u.save()

        return {'hello': u.phone}