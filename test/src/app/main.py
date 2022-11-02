#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 09:39
# @Author  : debugfeng
# @Site    : 
# @File    : main.py
# @Software: PyCharm

import uvicorn
from fastapi import FastAPI
from src.app.docs import tags_metadata
from src.app.routers.users import user
from src.app.routers.home import index
from src.app.routers.repuests import request
from src.app.routers.project import case, plan

app = FastAPI(
    title="Test测试平台接口文档", version="0.0.1", description="接口文档", openapi_tags=tags_metadata
)

app.include_router(router=user.router, tags=["用户模块"])
app.include_router(router=index.router, tags=["首页模块"])
app.include_router(router=request.router, tags=["接口测试模块"])
app.include_router(router=case.router, tags=["测试用例模块"])
app.include_router(router=plan.router, tags=["测试计划模块"])

if __name__ == '__main__':
    uvicorn.run(app="src.app.main:app", port=8086, host="0.0.0.0", debug=True)
