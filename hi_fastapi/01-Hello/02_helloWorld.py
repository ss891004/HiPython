# -*- coding: UTF-8 -*-
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def main():
    return {"message": "Helloworld，FastAPI"}
    

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=9988)

# pip install fastapi
# pip install uvicorn
