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
from functools import wraps
from json import JSONDecodeError
from src.app.public.logger import do_logger
from src.app.enumeration.request_enum import BodyType
from httpx import HTTPStatusError, RequestError, InvalidURL

__all__ = ["HttpRequest"]

# def _response(func):
#     @wraps(func)
#     def response_wraps(*args, **kwargs):
#         results = func(*args, **kwargs)
#         try:
#             return results.json()
#         except JSONDecodeError:
#             return results.text.encode("utf-8")
#         except Exception as ex:
#             do_logger.error(f"非json和text类型返回值: {ex}")
#             raise ex
#
#     return response_wraps


_loop = asyncio.get_event_loop()


class HttpRequest:
    def __init__(self):
        self.verify = False

    @classmethod
    def _handel_default_value(cls, *, params, **kwargs: typing.Any):
        # 判断params字段是否存在
        if not hasattr(kwargs, str(params)):
            results = kwargs.get(str(params))
            # 如果为真，则返回对应数据
            return results

    @classmethod
    def _default_headers(cls, *, body_type: BodyType, **kwargs: typing.Any):
        if not hasattr(kwargs, "headers"):
            # 把获取的数据转成字典
            headers = dict(kwargs.get("headers"))
            # 如果为真
            if headers:
                # 根据body_type的进行对比，然后执行更新操作
                match body_type:
                    case BodyType.json:
                        headers.update({"Content-Type": "application/json"})
                    case BodyType.form_urlencoded:
                        headers.update({"Content-Type": "application/x-www-form-urlencoded"})
                    case BodyType.form_data:
                        headers.update({"Content-Type": "multipart/form-data"})
                    case BodyType.binary:
                        headers.update({"Content-Type": "binary"})
                    case BodyType.graphQL:
                        headers.update({"Content-Type": "binary"})
                    case _:
                        pass
                return headers
            else:
                raise Exception("headers必须要存在")

    @classmethod
    def _default_files(cls, **kwargs: typing.Any):
        # 判断files字段是否存在
        if not hasattr(kwargs, "files"):
            files = kwargs.get("files")
            # 如果为真，则返回文件路径
            if files:
                # 判断路径是否为真
                if os.path.exists(files):
                    return files
                else:
                    raise Exception("请检查路径格式...")
            else:
                pass

    @classmethod
    def _default_body(cls, **kwargs: typing.Any):
        """
        处理body传参
        :param kwargs:
        :return:
        """
        if not hasattr(kwargs, "body"):
            body = kwargs.get("body")
            if body:
                try:
                    # 判断数据类型是不是字典，不是就转下，是就是直接返回
                    return kwargs.get("body") if isinstance(body, dict) else json.loads(body)
                except JSONDecodeError:
                    raise Exception("非json数据无法解析")
            else:
                pass

    @classmethod
    def _default_params(cls, **kwargs: typing.Any):
        """
        处理
        :param kwargs:
        :return:
        """
        if not hasattr(kwargs, "params"):
            params = kwargs.get("params")
            return params if params else None

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
            do_logger.info(
                f"""
                ----------------------------------------------------------------------
                请求方式：{response.request.method}
                请求 URL：{response.request.url}
                请求Header：{response.request.headers.multi_items()}
                请求参数：{ast.literal_eval(response.request.content.decode("utf-8"))}
                请求结果：{ast.literal_eval(response.content.decode("utf-8"))}
                ----------------------------------------------------------------------
                """
            )
            return response

    def request(self, *, method: str, url: str, body_type: BodyType, **kwargs: typing.Any):
        # 解决asyncio不允许它的事件循环被嵌套。允许嵌套使用asyncio.run和loop.run_until_complete。
        nest_asyncio.apply()

        # 判断url开头是不是http、https开头
        if not url.startswith(("http://", "https://")):
            raise Exception("请输入正确的url, 记得带上http或https")

        body, params = self._default_body(**kwargs), self._default_params(**kwargs)
        headers, files = self._default_headers(body_type=body_type, **kwargs), self._default_files(**kwargs)

        # 根据传参类型判断，然后执行请求接口操作
        match body_type:
            case BodyType.json:
                response = _loop.run_until_complete(
                    self._send_request_safe(method=method, url=url, json=body, params=params, headers=headers)
                )
                return self._response(response=response)

            case (BodyType.binary, BodyType.form_data.value, BodyType.form_urlencoded):
                if not files:
                    response = _loop.run_until_complete(
                        self._send_request_safe(method=method, url=url, data=body, params=params, headers=headers)
                    )
                    return self._response(response=response)
                else:
                    response = _loop.run_until_complete(
                        self._send_request_safe(
                            method=method, url=url, data=body, params=params, files=files, headers=headers
                        )
                    )
                    return self._response(response=response)
            case BodyType.graphQL:
                pass
            case _:
                response = _loop.run_until_complete(
                    self._send_request_safe(method=method, url=url, **kwargs)
                )
                return self._response(response=response)

    async def _send_request_safe(self, *, method: str, url: str, **kwargs: typing.Any):

        def _log_request(request):
            do_logger.info(f"Request: [ {request.method} : {request.url} ] ")

        def _log_response(response):
            request = response.request
            do_logger.info(f"Response: [ {request.method} : {request.url} ] - Status [ {response.status_code} ]")

        # 转化成大写
        methods = method.upper()
        # 超时时间默认设置 120 s
        kwargs.setdefault("timeout", 120)

        try:
            # 调用httpx库用于请求接口
            event_hooks = {'requests': [_log_request], 'response': [_log_response]}
            async with httpx.AsyncClient(event_hooks=event_hooks) as client:
                client.verify = self.verify
                return await client.send(client.build_request(methods, url, **kwargs))
        except (RequestError, InvalidURL) as ex:
            do_logger.error(f"请检查URL是否正确：{ex}")
            raise ex
        except HTTPStatusError as ex:
            raise ex
        except Exception as ex:
            do_logger.error(f"异常错误：{ex}")
            raise ex


if __name__ == '__main__':
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

    res = HttpRequest().request(
        method="get",
        url="https://api-lms3.9first.com/user/auth",
        body_type=BodyType.json,
        headers={"token": "74b354c22a87cab8c9cf6d80d5d9b018"})
    print(res)
