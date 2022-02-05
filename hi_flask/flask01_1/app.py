from flask import Flask
import settings

app = Flask(__name__)

app.config.from_object(settings)

@app.route('/')
def index():
    return "hello world. hello python"

if __name__=="__main__":
    app.run()