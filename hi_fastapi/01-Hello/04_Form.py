# -*- coding: UTF-8 -*-
from starlette.requests import Request
from fastapi import FastAPI, Form
from starlette.templating import Jinja2Templates

# 表单的填充，提交处理
# pip install python-multipart
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 用户填充表单，提交给后端
@app.post("/user/")
async def form_text(request: Request, username: str = Form(...), password: str = Form(...)):
    
    print('username',username)
    print('password',password)
    
    # return {'text_1':text_1 , 'text_2': text_2}
    return templates.TemplateResponse('04_home.html', {'request': request, 'username': username, 'password': password})


# 返回表单首页，用户填充表单
@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('04_post.html', {'request': request})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
