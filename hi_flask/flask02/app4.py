from flask import Flask,request
import settings

app = Flask(__name__)

app.config.from_object(settings)


# request 对象

@app.route("/index")
def index():
    print(request.headers)
    print(request.base_url)
    print(request.content_type)
    print(request.host)
    print(request.args)
    print(request.form)

    return "ok"


if __name__=="__main__":

    app.run()
