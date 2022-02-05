
import tornado.web
import tornado.ioloop
import tornado.httpclient


class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        q = self.get_argument('q')
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch('https://cn.bing.com/search?q=%s' % q, callback=self.on_response)
        self.write('异步测试')

    def on_response(self, response):
        # 回调，当页面响应，则调用回调函数on_response
        print(response)
        self.write('回调执行')
        self.finish()


def make_app():
    return tornado.web.Application(handlers=[
        (r'/index/', IndexHandler),
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
