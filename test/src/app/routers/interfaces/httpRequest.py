#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 18:03
# @Author  : debugfeng
# @Site    : 
# @File    : request.py
# @Software: PyCharm
import json

from fastapi import Depends
from fastapi import APIRouter
from src.app.utils.client import HttpRequest
from src.app.utils.fatcory import TestResponse
from src.app.schemas.httpSchemas import HttpBody
from src.app.dependencies.accessToken import AccessToken

router = APIRouter(
    prefix="/http",
    dependencies=[Depends(AccessToken.verify_token)]
)


@router.post("/request")
async def request_http(data: HttpBody):
    """
    请求HTTP协议接口
    :param data:
    :return:
    """
    try:
        response = HttpRequest().request(
            method=data.method, url=data.url, body=data.body,
            params=data.params, cookies=data.cookies, headers=data.headers, body_type=data.body_type
        )
        return TestResponse.successful(response=response)
    except Exception as ex:
        return TestResponse.defeated(msg=str(ex.args[0]))
