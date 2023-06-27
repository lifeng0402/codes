#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: cases_request.py
@时间: 2023/06/12 17:50:39
@说明:
"""

import json
import typing
import asyncio
from fastapi.encoders import jsonable_encoder
from src.app.cabinet.code_enum import RequestBody
from src.app.core.http_request import RequestHttp
from src.app.schemas.cases_schemas import BatchTestCaseRequest
from src.app.cabinet.data_transition import Transition


class Execute:
    def __init__(self) -> None:
        pass

    async def execute_run(self, test_cases: typing.List):
        if not test_cases:
            raise Exception("")

        tasks = [case for case in test_cases]
        # results = await asyncio.gather(*tasks)
        return tasks


a = "{\"token\": \"9d322f270932a2c3bcbbc532bbe899f8\", \"content_type\": \"application/json\"}"
b = "https://api-lms3.9first.com/manager/index/index/list"
c = None


print(json.dumps(c))
