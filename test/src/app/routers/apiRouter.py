#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: api.py
@时间: 2023/04/10 19:07:09
@说明: 
"""

from fastapi import APIRouter
from src.app.routers.interfaces import (
    user, project, plan, index, httpRequest, case
)

__all__ = ["api_router"]

api_router = APIRouter()
api_router.include_router(router=user.router, tags=["用户模块"])
api_router.include_router(router=index.router, tags=["首页模块"])
api_router.include_router(router=httpRequest.router, tags=["请求模块"])
api_router.include_router(router=case.router, tags=["用例模块"])
api_router.include_router(router=case.router, tags=["测试用例模块"])
api_router.include_router(router=plan.router, tags=["测试计划模块"])
api_router.include_router(router=project.router, tags=["项目管理模块"])
