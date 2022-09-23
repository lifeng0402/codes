#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 18:19
# @Author  : debugfeng
# @Site    : 
# @File    : client_request.py
# @Software: PyCharm
import json
from src.app.handler.client import HttpRequest
from src.app.handler.enum_fatcory import BodyType


class ClientRequest:

    def __init__(self, *, body_type: BodyType):
        self._body_type = body_type
        self._session = HttpRequest

    def client_request(self, *, method: str, url: str, **kwargs):
        if url.startswith(("http://", "https://")):
            return Exception(f"非正确的HTTP请求地址：{url}")

        body = kwargs.get("body")
        headers = kwargs.get("headers", {})
        if self._body_type == BodyType.json:
            if "Content-Type" not in headers:
                headers['Content-Type'] = "application/json; charset=UTF-8"
            try:
                if not body is None:
                    body = json.loads(body)
            except Exception as e:
                raise Exception(f"json格式不正确: {e}")

            return self._session(method=method, url=url, headers=headers, json=body)
        elif self._body_type == BodyType.form_data:
            if not body is None:
                body = json.loads(body)

