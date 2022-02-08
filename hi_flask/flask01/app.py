# 首先导入了Flask类，这个类的实例将会是一个WSGI应用。
from flask import Flask

# 接着创建一个该类的实例，传递给它模块或包的名称，这样Flask知道去哪里寻找模板、静态文件等。
app = Flask(__name__)

# 使用装饰器route()告诉Flask哪个URL才能触发函数。
@app.route("/hi")
# 定义一个函数，该函数名也是用来给特定函数生成URLs，并且返回我们想要显示在用户浏览器上的信息。
def test():
    return "hello flask, hello python"


if __name__ =="__main__":
    # 最后用函数run()启动本地服务器来运行Flask应用。
    app.run(host='0.0.0.0',port='3456',debug=TRUE)
