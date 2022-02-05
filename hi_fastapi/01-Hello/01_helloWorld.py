# -*- coding: UTF-8 -*-
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
    return {"message": "Helloworld，FastAPI ......"}

# pip install fastapi
# pip install uvicorn
# uvicorn 01_helloWorld:app --reload

# 01_helloWorld ：01_helloWorld.py 文件（一个 Python "模块"）。
# app：在 01_helloWorld.py 文件中通过 app = FastAPI() 创建的对象。
# --reload：让服务器在更新代码后重新启动。仅在开发时使用该选项。