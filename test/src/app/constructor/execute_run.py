#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/29 14:18
# @Author  : debugfeng
# @Site    : 
# @File    : execute_run.py
# @Software:

import ast
import json
import threading
import typing
from pydantic import HttpUrl

from src.app.handler.client import HttpRequest
from src.app.enumeration.request_enum import BodyType


class ExecuteRun:
    def __init__(self):
        self._http = HttpRequest()

    def _request_(self, method: str, url: HttpUrl, headers: dict, body_type: BodyType, **kwargs):
        results = self._http.request(method=method, url=url, headers=headers, body_type=body_type, **kwargs)
        status_code = results.status_code
        request_method = results.request.method
        response_url = results.url
        response_headers = results.headers
        match body_type:
            case (BodyType.json, BodyType.none):
                response = results.json()
            case (BodyType.binary, BodyType.form_data.value, BodyType.form_urlencoded):
                response = results.text
            case BodyType.binary:
                pass
            case _:
                response = results.text

    def execute(self, *, datas: typing.Any):
        for i in datas:
            case_id, title = i["id"], i["title"]
            method, url = i["method"], i["url"]
            body_type, headers = i["body_type"], ast.literal_eval(i["headers"])
            body = ast.literal_eval(i["body"]) if i["body"] else None
            params = ast.literal_eval(i["params"]) if i["params"] else None
            cookies = ast.literal_eval(i["cookies"]) if i["cookies"] else None
            actual, expect = i["actual"], i["expect"]

            t = threading.Thread(
                target=self._http.request, kwargs={
                    "method": method, "url": url, "headers": headers,
                    "body_type": body_type, "body": body, "params": params, "cookies": cookies
                }
            )
            t.start()
            print(t)
