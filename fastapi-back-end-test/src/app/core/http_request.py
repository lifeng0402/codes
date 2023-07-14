#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: request.py
@时间: 2023/06/10 17:54:19
@说明:
"""


import asyncio
from typing import (
    Dict,
    Any,
    Union
)
import json as js
from httpx import (
    Response, AsyncClient, Cookies, Headers
)
from pydantic import HttpUrl
from fastapi import HTTPException


__all__ = [
    "RequestHttp"
]


class RequestHttp:

    is_verify: bool = False

    @classmethod
    def handle_response(cls, status, response: Response, results):
        """
        收集返回值信息
        @param  :
        @return  :
        """
        return {
            "status": status,
            "request": {
                "method": response.request.method,
                "url": response.request.url,
                "headers": response.request.headers,
                "request": response.request.content
            },
            "response": {
                "method": response.request.method,
                "url": response.url,
                "headers": response.headers,
                "cookies": response.cookies,
                "response": results
            }
        }

    @classmethod
    def return_response(cls, response: Response):
        """
        验证返回值是不是json格式
        @param  :
        @return  :
        """
        try:
            return response.json()
        except js.JSONDecodeError:
            return response.text

    @classmethod
    async def safe_request(
            cls, method: str, url: HttpUrl, json: Dict = None, data: Dict = None, params: Dict = None,
            files=None, headers: Headers = None, timeout: float = None, cookies: Cookies = None, **kwargs
    ) -> Dict[str, Any]:
        """
        请求接口返回返回值
        @param  :
        @return  :
        """
        try:

            # 发送请求
            async with AsyncClient(verify=cls.is_verify) as client:

                method = method.upper()
                
                req_params = dict(
                    method=method, url=url, json=json, data=data,
                    params=params, headers=headers, timeout=timeout,
                    files=files, cookies=cookies, **kwargs
                )

                # 发送请求
                request = await client.request(**req_params)

                # 如果请求不成功后返回status为假的收集结果
                if not request.is_success:
                    return cls.handle_response(False, request, request)

                # 请求成功后返回status为真的收集结果
                return cls.handle_response(True, request, request)

        except Exception as exc:
            raise exc


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # response = loop.run_until_complete(requests())
    # print(response)
