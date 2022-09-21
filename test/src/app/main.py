#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 09:39
# @Author  : debugfeng
# @Site    : 
# @File    : main.py
# @Software: PyCharm

import uvicorn
from fastapi import FastAPI
# from src.app.models import BASE
from src.app.routers.users import user
# from src.app.public.databases import DATABASES

# 绑定连接，使用表元数据和引擎
# BASE.metadata.create_all(bind=DATABASES.ENGINE)

app = FastAPI()

app.include_router(router=user.router, tags=["用户模块"])


@app.get("/")
def index():
    return {"hello": "world"}


if __name__ == '__main__':
    uvicorn.run(app="src.app.main:app", port=8086, host="0.0.0.0", debug=True)
