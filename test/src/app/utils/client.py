#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 10:45
# @Author  : debugfeng
# @Site    :
# @File    : client.py
# @Software: PyCharm

import ast
import json
import os.path
import httpx
import typing
import asyncio
import nest_asyncio
from httpx import Response
from json import JSONDecodeError
from src.app.public.logger import do_logger
from src.app.enumeration.requestEnum import BodyType
from httpx import HTTPStatusError, RequestError, InvalidURL

__all__ = ["HttpRequest"]


class HttpRequest:

    def __init__(self):
        self.verify: bool = False

    @classmethod
    def _response(cls, response: Response):
        """
        处理返回值
        :param response:
        :return:
        """
        try:
            response.raise_for_status()
        except (RequestError, Exception) as ex:
            raise ex
        else:
            do_logger.info(f"""
                ----------------------------------------------------------------------
                请求方式:{response.request.method}
                请求 URL:{response.request.url}
                请求Header:{dict((k, v) for k, v in response.request.headers.multi_items())}
                请求参数：{ast.literal_eval(response.request.content.decode("utf-8"))}
                请求结果：{ast.literal_eval(response.content.decode("utf-8"))}
                ----------------------------------------------------------------------
                """)
            return response

    def request_safe(self, method: str, url: str, json=None, data=None, params=None, headers=None, **kwargs):
        """
        异步请求方法
        :param method:
        :param url:
        :param json:
        :param data:
        :param params:
        :param kwargs:
        :return:
        """
        # 判断url开头是不是http、https开头
        if not url.startswith(("http://", "https://")):
            raise Exception("请输入正确的url, 记得带上http或https")

        _loop = asyncio.get_event_loop()
        # 解决asyncio不允许它的事件循环被嵌套。允许嵌套使用asyncio.run和loop.run_until_complete。
        nest_asyncio.apply()
        return self._response(
            response=_loop.run_until_complete(
                self._send_request_safe(
                    method=method, url=url, json=json, data=data, params=params, headers=headers, **kwargs
                )
            )
        )

    async def _send_request_safe(self, *, method: str, url: str, **kwargs: typing.Any):
        """
        接口请求方法
        :param method:
        :param url:
        :param kwargs:
        :return:
        """

        def _log_request(request):
            do_logger.info(f"Request: [ {request.method} : {request.url} ] ")

        def _log_response(response):
            request = response.request
            do_logger.info(
                f"Response: [ {request.method} : {request.url} ] - Status [ {response.status_code} ]"
            )

        # 转化成大写
        methods = method.upper()
        # 超时时间默认设置 120 s
        kwargs.setdefault("timeout", 120)

        try:
            # 调用httpx库用于请求接口
            event_hooks = {
                'requests': [_log_request], 'response': [_log_response]
            }
            async with httpx.AsyncClient(event_hooks=event_hooks) as client:
                client.verify = self.verify
                return await client.send(
                    client.build_request(methods, url, **kwargs))
        except (RequestError, InvalidURL) as ex:
            do_logger.error(f"请检查URL是否正确:{ex}")
            raise ex
        except HTTPStatusError as ex:
            raise ex
        except Exception as ex:
            do_logger.error(f"异常错误:{ex}")
            raise ex


# if __name__ == '__main__':
# res = HttpRequest().request(
#     method="POST",
#     url="https://api-lms3.9first.com/user/auth",
#     body_type=BodyType.json,
#     headers={"Content-Type": "application/json; charset=UTF-8"},
#     body={
#         "user_name": "account01",
#         "password": "account01",
#         "scenario": "web",
#         "day": 1
#     })
# print(res)

# res = HttpRequest().request(
#     method="get",
#     url="https://api-lms3.9first.com/user/auth",
#     body_type=BodyType.json,
#     headers={"token": "74b354c22a87cab8c9cf6d80d5d9b018"})
# print(res)
