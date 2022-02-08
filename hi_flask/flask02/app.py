from flask import Flask
import settings

app = Flask(__name__)

app.config.from_object(settings)

@app.route('/')
def index():
    return "hello world. hello python"

# 路由的原理

def index2():
    return "welcome to index2.."
app.add_url_rule("/index2",view_func=index2)


if __name__=="__main__":

    app.run()
