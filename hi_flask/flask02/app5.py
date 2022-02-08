from flask import Flask
import settings

app = Flask(__name__)

app.config.from_object(settings)


# jinja2 模板引擎



if __name__=="__main__":

    app.run()
