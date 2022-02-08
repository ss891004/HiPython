from flask import Flask
import settings

app = Flask(__name__)
app.config.from_object(settings)

# 路由最后的 / 的问题

# http://127.0.0.1:5000/index  200
# http://127.0.0.1:5000/index/ 404

@app.route("/index")
def index():
    return "index....."



# http://127.0.0.1:5000/index2    308 -> 200
# http://127.0.0.1:5000/index2/   200

@app.route("/index2/")
def index2():
    return "index2....."


if __name__=="__main__":

    app.run()
