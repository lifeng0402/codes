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
    Any
)
import json as js
from httpx import (
    Response, AsyncClient
)
from pydantic import HttpUrl


__all__ = [
    "RequestHttp"
]


class RequestHttp:

    is_verify: bool = False
    is_response: bool = False

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
        cls, method: str, url: HttpUrl, json=None, data=None, params=None,
        content=None, files=None, headers=None, cookies=None, timeout=30, **kwargs
    ) -> Dict[str, Any]:
        """
        请求接口返回返回值
        @param  :
        @return  :
        """
        method = method.upper()
        if not url.startswith("https://", "http://"):
            raise Exception("请求地址必须要包含https或http...")

        # 发送请求
        async with AsyncClient(verify=cls.is_verify) as client:
            request = await client.request(
                method, url, data=data, json=json, params=params, content=content,
                files=files, headers=headers, cookies=cookies, timeout=timeout, **kwargs
            )

            # 如果为真则直接返回结果, 否则就是返回收集后的返回结果
            if cls.is_response:
                return cls.return_response(response=request)

            # 如果请求不成功后返回status为假的收集结果
            if not request.is_success:
                return cls.handle_response(False, request, request)

            # 请求成功后返回status为真的收集结果
            return cls.handle_response(True, request, request)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # response = loop.run_until_complete(requests())
    # print(response)
