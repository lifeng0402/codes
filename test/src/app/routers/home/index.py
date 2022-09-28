#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 08:27
# @Author  : debugfeng
# @Site    : 
# @File    : index.py
# @Software: PyCharm

from fastapi import Depends
from fastapi import APIRouter
from src.app.handler.fatcory import TestResponse
from src.app.dependencies.access_token import AccessToken

router = APIRouter(
    dependencies=[Depends(AccessToken.verify_token)]
)


@router.get("/")
async def index():
    try:
        return TestResponse.successful(msg="欢迎来到 1024 测试平台 ...", data={})
    except Exception as e:
        return TestResponse.defeated(msg=str(e.args[0]), data={})
