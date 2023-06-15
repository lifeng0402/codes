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
    Mapping,
    Optional,
    Dict,
    Any,
    Union
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
from src.app.schemas.cases_schemas import RequestSchemas


__all__ = [
    "safe_request"
]


class RequestHttp:
    def __init__(self, method: str, url: HttpUrl, is_response: bool = False) -> None:
        self._method:str = method
        self._url: HttpUrl = url
        self._is_response = is_response

    async def safe_request(
        self,
        data: Optional[Union[bytes, str]] = None,
        json: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        请求接口返回返回值
        @param  :
        @return  :
        """

        def handle_response(status, response: Response, results):
            """
            收集返回值信息
            @param  :
            @return  :
            """
            return {
                "status": status,
                "requet": {
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

        url = self._url
        method = self._method.upper()

        async with AsyncClient() as client:
            request = await client.request(
                method,
                url,
                data=data,
                json=json,
                params=params,
                headers=headers,
                timeout=timeout,
                **kwargs
            )

            # 如果为真则直接返回结果, 否则就是返回收集后的返回结果
            if self._is_response:
                return RequestHttp.return_response(response=request)

                # 如果请求不成功后返回status为假的收集结果
            if not request.is_success:
                return handle_response(False, request, request)
                # 请求成功后返回status为真的收集结果
            return handle_response(True, request, request)

    @staticmethod
    def return_response(response: Response):
        try:
            return response.json()
        except js.JSONDecodeError:
            return response.text
        except Exception as e:
            raise e


async def safe_request(*, datas: RequestSchemas, is_response: bool = False):
    """
    调用继承后的基类, 用于请求接口
    @param  :
    @return  :
    """

    try:
        # 初始化一个请求方法
        request = RequestHttp(
            url=datas.url,
            method=datas.method,
            is_response=is_response
        )

        if RequestBody.raw == datas.body_type:
            response = await request.safe_request(
                json=datas.body,
                params=datas.params,
                headers=datas.headers,
                cookies=datas.cookies,
                timeout=datas.timeout,
                extensions=datas.extensions
            )
        elif RequestBody.binary == datas.body_type:
            response = await request.safe_request(
                json=datas.body,
                params=datas.params,
                headers=datas.headers,
                cookies=datas.cookies,
                timeout=datas.timeout,
                extensions=datas.extensions
            )
        elif RequestBody.graphql == datas.body_type:
            response = await request.safe_request(
                json=datas.body,
                params=datas.params,
                headers=datas.headers,
                cookies=datas.cookies,
                timeout=datas.timeout,
                extensions=datas.extensions
            )
        elif RequestBody.form_data == datas.body_type or RequestBody.x_www_form_urlencoded == datas.body_type:
            response = await request.safe_request(
                data=datas.body,
                files=datas.files,
                params=datas.params,
                headers=datas.headers,
                cookies=datas.cookies,
                timeout=datas.timeout,
                extensions=datas.extensions
            )
        else:
            response = await request.safe_request(
                params=datas.params,
                headers=datas.headers,
                cookies=datas.cookies,
                timeout=datas.timeout,
                extensions=datas.extensions
            )
            # 返回值
        return response

    except Exception as exc:
        raise exc


# async def requests():
#     response = await RequestHttp().safe_request(method="GET", url="https://www.baidu.com/")
#     print("Response code:", response)
#     return response


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # response = loop.run_until_complete(requests())
    # print(response)
