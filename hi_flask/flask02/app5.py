from flask import Flask,render_template
import settings

app=Flask(__name__) # 默认是 当前目录下的 templates文件夹
#app = Flask(__name__,template_folder="template")
#app = Flask(__name__,template_folder="../tmps")


app.config.from_object(settings)

# jinja2 模板引擎

@app.route("/index")
def index():
    user ={"username":"hi  shishuai ~~~~~"}
    return render_template("index.html",xxx=user)


@app.route('/index2')
def index2():
    # 往模板中传入的数据
    my_str = 'Hello word'
    my_int = 10
    my_array = [3, 4, 2, 1, 7, 9]
    my_dict = {
        'name': 'xiaoming',
        'age': 18
    }
    return render_template('index2.html',
                           my_str=my_str,
                           my_int=my_int,
                           my_array=my_array,
                           my_dict=my_dict
                           )




if __name__=="__main__":
    print(app.url_map)
    app.run()
