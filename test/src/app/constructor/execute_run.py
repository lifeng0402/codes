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
from fastapi import status
from src.app.constructor import affirm
from src.app.handler.client import HttpRequest
from src.app.enumeration.request_enum import BodyType


class ExecuteRun:
    def __init__(self):
        self._http = HttpRequest()
        self._actual = None
        self._expect = None
        self._comparison = None

    def _request_(self, method: str, url: HttpUrl, headers: dict, body_type: BodyType, **kwargs):

        results = self._http.request(method=method, url=url, headers=headers, body_type=body_type, **kwargs)

        if results.is_success:
            match body_type:
                case (BodyType.json):
                    response = results.json()
                    affirm.self_main(comparison=self._comparison, expect=self._expect, actual=response)
                    return response
                case (BodyType.binary, BodyType.form_data.value, BodyType.form_urlencoded):
                    response = results.text
                    return response
                case BodyType.binary:
                    pass
                case _:
                    response = results.text
                    return response
        if results.is_error or results.is_client_error or results.is_server_error:
            return results.content.decode("utf-8")


def execute(self, *, response: typing.Any):
    for items in response:
        case_id, title, datas = items["id"], items["name"], items["datas"]
        self._actual, self._expect, self._comparison = items["actual"], items["expect"], items["expect"]
        is_success, is_error, exception = items["is_success"], items["is_error"], items["exception"]

        self._request_()

        for item in datas:
            t = threading.Thread(target=self._request_, kwargs=item)
            t.start()
            print(t)
