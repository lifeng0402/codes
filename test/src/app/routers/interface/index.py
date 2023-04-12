#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 08:27
# @Author  : debugfeng
# @Site    : 
# @File    : index.py
# @Software: PyCharm

from fastapi import Depends
from fastapi import APIRouter
from src.app.utils.fatcory import TestResponse
from src.app.dependencies.accessToken import AccessToken

router = APIRouter(
    dependencies=[Depends(AccessToken.verify_token)]
)


@router.get("/")
async def index():
    try:
        return TestResponse.successful(
            data=dict(info="欢迎来到 1024 测试平台 ...")
            )
    except Exception as e:
        return TestResponse.defeated()
