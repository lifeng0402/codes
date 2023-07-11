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
from typing import Optional, Callable, Any
from src.app.routers.api_router import api_router

app = FastAPI()


@app.middleware
async def add_header(request: Request, response: Response, next: Optional[Callable[..., Any]]):
    headers = {"Content-Type": "application/json"}
    request.headers.update(headers)
    response.headers.update(headers)
    return await next(response)


app.include_router(router=api_router)


if __name__ == "__main__":
    uvicorn.run(app="src.main:app", reload=True)
