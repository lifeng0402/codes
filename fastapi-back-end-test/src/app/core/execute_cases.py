#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: cases_request.py
@时间: 2023/06/12 17:50:39
@说明:
"""

import json
import asyncio
import typing as ty
import concurrent.futures
from fastapi.encoders import jsonable_encoder
from src.app.schemas.case import RequestBase
from src.app.core.http_request import RequestHttp
from src.app.schemas.case import TestCaseRequest
from src.app.cabinet.transition import Transition


async def execute(list_results: ty.List[dict]):

    total, succeed, defeated, error = (0, 0, 0, 0)

    for req in list_results["list"]:

        req_params = dict(
            url=req.get("url"),
            method=req.get("method"),
            json=req.get("json_data"),
            data=req.get("form_data"),
            params=req.get("params"),
            files=req.get("files"),
            content=req.get("content"),
            headers=json.loads(req.get("headers")),
            cookies=req.get("cookies"),
            timeout=req.get("timeout"),
        )

        expected_result = req.get("expected_result")

        response = await RequestHttp.safe_request(**req_params)

        response_status = response["status"]

        if not expected_result:
            pass

    print(total, succeed, defeated, error)


if __name__ == "__main__":
    a = {
        'method': 'GET',
        'url': 'https://api-lms3.9first.com/manager/index/index/list',
        'body_type': '0',
        'body': None,
        'params': None,
        'headers': '{"token": "9d322f270932a2c3bcbbc532bbe899f8", "content_type": "application/json"}',
        'cookies': None,
        'content': None,
        'files': None,
        'expected_result': None
    }
