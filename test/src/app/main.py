#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 09:39
# @Author  : debugfeng
# @Site    :
# @File    : main.py
# @Software: PyCharm


import asyncio
import uvicorn
from fastapi import FastAPI
from src.app.docs import tags_metadata
from src.app.routers import (
    user, index, httpRequest, case, plan
)

app = FastAPI(
    title="1024测试平台接口文档", version="0.0.1",
    description="接口文档", openapi_tags=tags_metadata
)

app.include_router(router=user.router, tags=["用户模块"])
app.include_router(router=index.router, tags=["首页模块"])
app.include_router(router=httpRequest.router, tags=["请求模块"])
app.include_router(router=case.router, tags=["用例模块"])
app.include_router(router=case.router, tags=["测试用例模块"])
app.include_router(router=plan.router, tags=["测试计划模块"])


async def main():
    config = uvicorn.Config(
        app="src.app.main:app", port=8086,
        host="10.10.29.245", log_level="info", reload=True
    )
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == '__main__':
    asyncio.run(main())
