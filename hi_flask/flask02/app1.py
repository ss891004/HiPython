from flask import Flask
import settings

# 路由的变量规则

app = Flask(__name__)

app.config.from_object(settings)

aaa={'a':'北京','b':'上海','c':"南通"}

@app.route('/get/<key>')
def index(key):
    return  aaa.get(key)


@app.route('/add/<int:key>')
def add(key):
    return str(key+10)  # 不能直接返回int类型的数据

if __name__=="__main__":
    print(app.url_map)
    app.run()
