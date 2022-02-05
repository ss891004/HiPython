from wsgiref.simple_server import make_server
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

httpd = make_server('127.0.0.1', 12345, application)
# 开始监听HTTP请求:
httpd.serve_forever()

# 什么是WSGI(Web Server Gateway Interface)