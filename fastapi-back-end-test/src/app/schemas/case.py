#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: cases_schemas.py
@时间: 2023/06/10 16:56:08
@说明: 
"""

from typing import Any
from pydantic import (
    HttpUrl, validator
)
from src.app.cabinet.enumerate import (
    Headers,
    Checkout,
    Extractors,
    Cookies,
    ExpectedResult,
    JsonData,
    FormData
)
from dataclasses import dataclass


__all__ = [
    "RequestBase",
    "RequestSchemas",
    "DeleteCases",
    "BatchTestCaseRequest",
    "CasesRunRequest"
]


@dataclass
class RequestBase:
    method: str
    url: HttpUrl
    json_data: JsonData = None
    form_data:  FormData = None
    headers: Headers = None
    content: Any = None
    files: Any = None
    params: Any = None
    cookies: Cookies = None
    timeout: Any = None
    extract: Extractors = None
    checkout: Checkout = None
    expected_result: ExpectedResult = None

    @validator('method', 'url')
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise Exception(f"{v} 不能为空")
        return v


@dataclass
class RequestSchemas(RequestBase):
    plan_id: int = None


@dataclass
class DeleteCases:
    case_ids: list[int]

    @validator('case_ids')
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise Exception(f"{v} 不能为空")
        return v


@dataclass
class TestCaseRequest:
    case_ids: list[RequestBase]


@dataclass
class BatchTestCaseRequest:
    plan_id: int = None


@dataclass
class CasesRunRequest:
    case_ids: list[int]
    plan_id: int = None

    @validator('case_ids')
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise Exception(f"{v} 不能为空")
        return v
