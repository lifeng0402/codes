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
    Union,
    List,
    Tuple
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
from ssl import SSLContext
from pydantic import HttpUrl
from src.app.cabinet.code_enum import RequestBody
from src.app.schemas.cases_schemas import RequestSchemas


__all__ = [
    "SafeRequest"
]


class RequestHttp:
    def __init__(
            self,
            method: str,
            url: HttpUrl,
            headers: Optional[Dict[str, str]],
            cookies: Optional[
                Union[Dict[str, str], List[Tuple[str, str]]]] = None,
            timeout: Optional[float] = None,
            verify: bool = False,
            is_response: bool = False
    ) -> None:
        self._method = method
        self._url = url
        self._headers = headers
        self._cookies = cookies
        self._timeout = timeout
        self._verify = verify
        self._is_response = is_response

    async def safe_request(
        self,
        data: Optional[Union[bytes, str]] = None,
        json: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
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

        method, url = self._method.upper(), self._url
        headers, cookies, timeout = self._headers, self._cookies, self._timeout

        async with AsyncClient(verify=self._verify) as client:
            request = await client.request(
                method, url, data=data, json=json, params=params,
                headers=headers, cookies=cookies, timeout=timeout, **kwargs
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


class SafeRequest:

    @classmethod
    def proof_json(cls, data: str):
        try:
            if not data:
                return data
            return js.dumps(data, indent=4)
        except js.JSONDecodeError:
            raise js.JSONDecodeError("请求参数非json类型")

    @classmethod
    async def safe_request(cls, *, datas: RequestSchemas, is_response: bool = False):
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
                headers=datas.headers,
                cookies=datas.cookies,
                timeout=datas.timeout,
                is_response=is_response
            )
            # 判断body_type的类型是否符合
            match datas.body_type:
                case RequestBody.raw:
                    json_data = cls.proof_json(datas.body)
                    response = await request.safe_request(
                        json=json_data,
                        params=datas.params,
                        extensions=datas.extensions
                    )

                case RequestBody.binary:
                    response = await request.safe_request(
                        json=datas.body,
                        params=datas.params,
                        extensions=datas.extensions
                    )

                case RequestBody.graphql:
                    response = await request.safe_request(
                        json=datas.body,
                        params=datas.params,
                        extensions=datas.extensions
                    )

                case [RequestBody.form_data, RequestBody.x_www_form_urlencoded]:
                    response = await request.safe_request(
                        data=datas.body,
                        files=datas.files,
                        params=datas.params,
                        extensions=datas.extensions
                    )

                case _:
                    response = await request.safe_request(
                        params=datas.params,
                        extensions=datas.extensions
                    )
            # 返回值
            return response

        except Exception as exc:
            raise exc


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # response = loop.run_until_complete(requests())
    # print(response)