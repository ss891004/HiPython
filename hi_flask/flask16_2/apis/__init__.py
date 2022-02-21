
from flask_restx import Api
from .message import ns as msg_ns
from .hello_world import HelloWorld

api =Api()

def init_api(app):
    api.init_app(app, version='1.0', title='flask rest',description='a spec flask rest',)

api.add_namespace(msg_ns,path='/a')

api.add_resource(HelloWorld,'/b')