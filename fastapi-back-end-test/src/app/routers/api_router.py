#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: api_router.py
@时间: 2023/06/01 16:52:49
@说明: 
"""


from fastapi import APIRouter
from src.app.routers.users import (
    register,
    login
)
from src.app.routers.home import (
    index
)


api_router = APIRouter()
api_router.include_router(router=register.router, tags=["注册接口"])
api_router.include_router(router=login.router, tags=["登录接口"])
api_router.include_router(router=index.router, tags=["首页接口"])
