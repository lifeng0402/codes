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

    for rq in list_results["list"]:
        method = rq.method
        url = rq.url
        body_type = rq.body_type
        files = rq.files
        timeout = rq.timeout
        body = Transition.proof_dict(rq.body),
        params = Transition.proof_dict(rq.params),
        headers = Transition.proof_dict(rq.headers),
        cookies = Transition.proof_dict(rq.cookies),

        expected_result = Transition.proof_dict(rq.expected_result)

        print(rq.url)

        response = await RequestHttp.safe_request(
            method=method, url=url, body_type=body_type, files=files, timeout=timeout,
            body=body, params=params, headers=headers, cookies=cookies
        )
    else:
        if not response["status"]:
            return response

        if expected_result:
            response["response"]["response"]

        return response


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
