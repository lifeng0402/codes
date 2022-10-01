#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 18:03
# @Author  : debugfeng
# @Site    : 
# @File    : request.py
# @Software: PyCharm

from fastapi import APIRouter
from src.app.schemas.http.http_schemas import HttpBody
from src.app.handler.client import HttpRequest
from src.app.handler.fatcory import TestResponse

router = APIRouter(
    prefix="/http"
)


@router.post("/request")
async def request_http(data: HttpBody):
    try:
        response = HttpRequest(
            method=data.method, url=data.url,
            body_type=data.body_type, headers=data.headers,
            body=data.body
        ).request.json()
        return TestResponse.successful(response=response)
    except Exception as e:
        return TestResponse.defeated(msg=str(e.args[0]), data={})
