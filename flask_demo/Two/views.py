from flask import Blueprint


two_first = Blueprint('two_first', __name__)


@two_first.route('/two/')
def index():
    return ' two First Blue'
 


two_second = Blueprint('two_second', __name__)

@two_second.route('/two/hello/')
def hello():
    return ' two Second Blue'



two_third = Blueprint('two_third', __name__)

@two_third.route('/two/htird/')
def hi():
    return 'two Third Blue'