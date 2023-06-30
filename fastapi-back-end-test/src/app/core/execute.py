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
from src.app.core.http_request import safe_request
from src.app.schemas.case import TestCaseRequest
from src.app.cabinet.transition import Transition


class Execute:

    @classmethod
    async def execute(cls, datas: dict):
        method = datas.get("method")
        url = datas.get("url")
        body_type = datas.get("body_type")
        files = datas.get("files")
        timeout = datas.get("timeout")
        body = Transition.proof_dict(datas.get("body"))
        params = Transition.proof_dict(datas.get("params"))
        headers = Transition.proof_dict(datas.get("headers"))
        cookies = Transition.proof_dict(datas.get("cookies"))
        expected_result = Transition.proof_dict(datas.get("expected_result"))

        response = await safe_request(
            method=method, url=url, body_type=body_type, body=body, params=params, headers=headers,
            cookies=cookies, files=files, timeout=timeout
        )



        if response["status"]:
            if expected_result:
                response["response"]["response"] 
            
            
        return response

    @classmethod
    async def run(cls, test_cases: TestCaseRequest):
        if not test_cases:
            raise Exception("")

        total: int = 0
        for case in test_cases:
            response = await cls.execute(case)

            status = response.get("status")
        # response = await asyncio.gather(results)
        # return results
        return results


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
    loop = asyncio.get_event_loop()
    response = loop.run_until_complete(Execute().execute(a))
    print(response)
    print()
