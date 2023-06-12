#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: cases_request.py
@时间: 2023/06/12 17:50:39
@说明: 
"""

from src.app.public.send_request import RequestHttp
from src.app.schemas.cases_schemas import RequestSchemas


class CasesRequest:

    def __init__(self) -> None:
        pass

    async def case_request(self, datas: RequestSchemas):
        async with RequestHttp() as client:
            resutls = await client.safe_request(
                method=datas.method,
                url=datas.url,
                content=datas.content,
                data=datas.data,
                files=datas.files,
                json=datas.json_data,
                params=datas.params,
                headers=datas.headers,
                cookies=datas.cookies,
                timeout=datas.timeout,
                auth=datas.auth,
                follow_redirects=datas.follow_redirects,
                extensions=datas.extensions,
            )
            return resutls.json()
