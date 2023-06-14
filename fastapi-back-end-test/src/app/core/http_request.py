#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: request.py
@时间: 2023/06/10 17:54:19
@说明:
"""


import json as js
import asyncio
from typing import (
    Optional,
    Any,
    Mapping
)
from httpx import (
    URL,
    Headers,
    Cookies,
    Timeout,
    Response,
    Request,
    AsyncClient
)
from pydantic import HttpUrl
from src.app.cabinet.code_enum import RequestBody
from src.app.schemas.cases_schemas import BodySchemas


__all__ = [
    "safe_request"
]


class RequestHttp:
    def __init__(self) -> None:
        self._client = AsyncClient()

    async def safe_request(self, *, method: str, url: HttpUrl, **kwargs):

        method = method.upper()
        kwargs["json"] = kwargs.pop("json_data")

        async with self._client as c:
            request = await c.request(method=method, url=url, **kwargs)
            response = RequestHttp.return_response(response=request)

            if not request.is_success:
                return RequestHttp.handle_response("defeated", request, response)
            return RequestHttp.handle_response("succeed", request, response)

    @staticmethod
    def return_response(response: Response):
        try:
            return response.json()
        except js.JSONDecodeError:
            return response.text
        except Exception as e:
            raise e

    @staticmethod
    def handle_response(status, response: Response, results):
        return {
            "status": status,
            "requet": {
                "url": response.request.url,
                "headers": response.request.headers.raw,
                "request": response.request.content
            },
            "response": {
                "url": response.url,
                "headers": response.headers.raw,
                "cookies": response.cookies,
                "response": results
            }
        }


async def safe_request(*, datas: BodySchemas):
    """
    调用继承后的基类, 用于请求接口
    @param  :
    @return  :
    """
    try:
        # 请求方法
        request = await RequestHttp().safe_request(
                method=datas.body.method,
                url=datas.body.url,
                data=datas.body.data,
                json_data=datas.body.json_data,
                params=datas.body.params,
                files=datas.body.files,
                headers=datas.body.headers,
                cookies=datas.body.cookies,
                timeout=datas.body.timeout,
                extensions=datas.body.extensions
        )
        # 返回值
        return request

    except Exception as exc:
        raise exc


async def requests():
    response = await RequestHttp().safe_request(method="GET", url="https://www.baidu.com/")
    print("Response code:", response)
    return response


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    response = loop.run_until_complete(requests())
    print(response)
