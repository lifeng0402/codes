#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: send_request.py
@时间: 2023/07/13 19:07:53
@说明:
"""

from src.app.cabinet.enumerate import BodyType
from src.app.core.http_request import RequestHttp


def send_request(method: str, url: str, body_type: int, body=None, headers=None, files=None, cookies=None):
    req = RequestHttp()

    match body_type:
        case BodyType.none:
            pass
        case BodyType.form_data:
            pass
        case BodyType.x_form_url:
            pass
        case BodyType.binary:
            pass
        case BodyType.graphql:
            pass
        case _:
            raise Exception("暂时不支持此类型...")

    req.safe_request(method=method, url=url, )
