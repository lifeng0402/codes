#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 10:45
# @Author  : debugfeng
# @Site    : 
# @File    : client.py
# @Software: PyCharm
import json

from httpx import Client
from typing import Union, Optional
from src.app.public.logger import do_logger
from src.app.handler.enum_fatcory import BodyType

__all__ = ["HttpRequest"]


class HttpRequest:
    def __init__(
            self, *, method, url, body_type, content=None, body=None, files=None,
            params=None, headers=None, cookies=None, timeout=None, extensions=None
    ):

        """

        :param method:
        :param url:
        :param body_type:
        :param content:
        :param files:
        :param body:
        :param params:
        :param headers:
        :param cookies:
        :param timeout:
        :param extensions:
        """
        self._method: str = method
        self._url: str = url
        self._content: str = content
        self._body: Optional[Union[str, dict]] = body
        self._files = files
        self._body_type: BodyType = body_type
        self._params: Optional[Union[str, int, float, bool]] = params
        self._headers: dict = headers
        self._cookies: Union[dict[str, str], list[tuple[str, str]]] = cookies
        # 验证SSL证书，默认不验证
        self.verify: bool = False
        self._timeout: Union[float, int] = timeout
        self._extensions = extensions

    @property
    def _differentiate(self):
        """
        区分json和form-data格式数据
        :return:
        """
        return self._body if self._body_type == BodyType.json else None

    @property
    def request(self):
        """
        请求接口方法
        :return:
        """
        try:
            with Client(verify=self.verify) as client:
                request = client.build_request(
                    method=self._method, url=self._url, content=self._content,
                    data=self._differentiate, files=self._files, json=self._differentiate, params=self._params,
                    headers=self._headers, cookies=self._cookies, timeout=self._timeout, extensions=self._extensions
                )
                results = client.send(request)
            return results
        except Exception as e:
            do_logger.error(str(e))
            raise e


if __name__ == '__main__':
    res = HttpRequest(
        method="post",
        url="https://api-lms3.9first.com/user/auth",
        body={
            "user_name": "account01",
            "password": "account01",
            "scenario": "web",
            "day": 1
        }
    ).request
    print(res.json())
