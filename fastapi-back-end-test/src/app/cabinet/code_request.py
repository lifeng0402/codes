#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: code_request.py
@时间: 2023/06/10 16:46:35
@说明: 
"""


from httpx import AsyncClient
from httpx import Response
from httpx import Request


__all__ = [

    "HttpClent",
    "HttpRequest",
    "HttpResponse"

]


class HttpClent(AsyncClient):
    pass


class HttpRequest(Request):
    pass


class HttpResponse(Response):
    pass
