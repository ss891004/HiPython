from flask import Flask,Response,make_response
import settings

app = Flask(__name__)

app.config.from_object(settings)

# response 对象


@app.route("/index")
def index():
    r= Response("aaaaa")
    print(r.content_type)
    print(r.status)
    print(r.headers)
    print(r.expires)
    return r


if __name__=="__main__":

    app.run()
