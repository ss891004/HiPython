from flask_restx import Resource,marshal_with,fields,expect
from models.user import User
from flask_restx.namespace import expect



reps_user = {
    'id':fields.String,
    'username':fields.String,
    'password':fields.String,
    'insert_time' : fields.DateTime,
    'tel_phone': fields.String
}

# 类视图  CBV（class base views）
class HelloWorld(Resource):
    @marshal_with(reps_user)
    def get(self):
        return User.query.all() 

    @expect(parser)
    def post(self):
        return {'hello': 'world'}