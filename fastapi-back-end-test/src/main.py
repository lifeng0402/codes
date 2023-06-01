#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: main.py
@时间: 2023/06/01 16:52:41
@说明: 
"""

import uvicorn
from fastapi import FastAPI
from src.app.routers.api_router import api_router

app = FastAPI()
app.include_router(router=api_router)

if __name__ == "__main__":
    uvicorn.run(app="src.main:app", reload=True)
