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
from src.app.routers.api import api_router
from src.app.config import settings as st

app = FastAPI(
    **st.FASTAPI_TEXT_DICT,
    openapi_tags=tags_metadata
)

app.include_router(router=api_router)


async def main():
    server = uvicorn.Server(
        config=uvicorn.Config(
            app="src.app.main:app", host="10.10.29.245", port=8086,  log_level="info", reload=True
        )
    )
    await server.serve()


if __name__ == '__main__':
    asyncio.run(main())
