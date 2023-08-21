#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: main.py
@时间: 2023/06/01 16:52:41
@说明: 
"""

import uvicorn
from fastapi import (
    FastAPI,
    Request,
    Response
)
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from typing import Optional, Callable, Any
from src.app.routers.api_router import api_router

app = FastAPI()

origins = [
    "http://localhost:3000",
    # "http://127.0.0.1:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.middleware
async def add_header(request: Request, response: Response, next: Optional[Callable[..., Any]]):
    headers = {"Content-Type": "application/json"}
    request.headers.update(headers)
    response.headers.update(headers)
    return await next(response)


# @app.middleware("http")
# async def log_requests(request, call_next):
#     response = await call_next(request)

#     # 记录请求日志
#     print(response)
#     logger.info(
#         f"{request.method} {request.url.path} - {response.status_code}"
#     )

#     return response

app.include_router(router=api_router)


if __name__ == "__main__":
    uvicorn.run(app="src.main:app", reload=True)
