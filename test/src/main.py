#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 09:39
# @Author  : debugfeng
# @Site    :
# @File    : main.py
# @Software: PyCharm

import os
import sys
import asyncio
import uvicorn
from config import Confing
from fastapi import FastAPI
from docs.doc import TagMetadata
from src.app.routers.apiRouter import api_router


sys.path.insert(0, os.path.dirname(os.path.dirname(os.getcwd())))
# print(sys.path)

app = FastAPI(
    **Confing.FASTAPI_TEXT_DICT,
    openapi_tags=TagMetadata.tags_metadata
)

app.include_router(router=api_router)


async def main():
    server = uvicorn.Server(
        config=uvicorn.Config(
            app=Confing.SERVER_APP, 
            host=Confing.SERVER_HOST, 
            port=Confing.SERVER_PORT,  
            log_level=Confing.SERVER_LOG_LEVEL, reload=True
        )
    )
    await server.serve()


if __name__ == '__main__':
    asyncio.run(main())
