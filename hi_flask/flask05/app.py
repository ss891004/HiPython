from exts import create_app


## 程序入口  export FLASK_APP=app.py  flask run 
app = create_app()


# if __name__ == "__main__":
#     print(app.url_map)
#     app.run(debug=True)