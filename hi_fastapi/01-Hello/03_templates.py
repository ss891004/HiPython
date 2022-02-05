# -*- coding: UTF-8 -*-
from starlette.requests import Request
from fastapi import FastAPI
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('03_index.html', {'request': request, 'hello': 'HI...'})

@app.get("/{item_id}/")
async def item_id(request: Request, item_id):
    return templates.TemplateResponse('03_index.html', {'request': request, "item_id": item_id})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# pip install -U Jinja2
'''
使用jinja2的模板，模板中使用占位符，python 后段经过处理，将对应的占位符的内容在模板中替换。
'''
