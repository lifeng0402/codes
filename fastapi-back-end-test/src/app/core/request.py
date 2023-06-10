#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: request.py
@时间: 2023/06/10 17:54:19
@说明: 
"""


from httpx import AsyncClient

class RequestHttp:
    def __init__(self) -> None:
        self._session = AsyncClient()

    async def requests(self):
        self._session.build_request()