#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: api_router.py
@时间: 2023/06/01 16:52:49
@说明: 
"""


from fastapi import APIRouter
from src.app.routers.v_api import (
    api_home, api_users
)
from src.app.routers.v_api.projects import (
    api_cases, api_plans, api_request
)


api_router = APIRouter()
api_router.include_router(router=api_users.router, tags=["用户模块接口"])
api_router.include_router(router=api_home.router, tags=["首页模块接口"])
api_router.include_router(router=api_request.router, tags=["请求接口"])
api_router.include_router(router=api_cases.router, tags=["测试用例模块接口"])
api_router.include_router(router=api_plans.router, tags=["测试计划模块接口"])
