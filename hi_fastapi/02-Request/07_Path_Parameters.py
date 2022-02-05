# -*- coding: UTF-8 -*-
from fastapi import FastAPI
from enum import Enum
import uvicorn

app = FastAPI()

# 请求参数- 路径参数
# Web交互式文档  http：//ip:port/docs
class Name(str, Enum):
    Allan = '张三'
    Jon   = '李四'
    Bob   = '王五'

# 从上到下依次匹配
@app.get("/me/xx")
async def read_item_me():
    return {"me": 'me'}

@app.get("/me/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}

@app.get("/w/{who}")
async def get_day(who: Name):
    if who == Name.Allan:
        return {"who": who, "message": "张三是德国人"}
    if who.value == '李四':
        return {"who": who, "message": "李四是英国人"}
    return {"who": who, "message": "王五是法国人"}


@app.get("/")
async def main():
    return {"message": "Hello，FastAPI"}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)




