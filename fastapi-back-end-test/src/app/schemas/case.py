#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: cases_schemas.py
@时间: 2023/06/10 16:56:08
@说明: 
"""

from typing import (
    Optional,
    Any,
    List,
    Union,
    Dict
)
from pydantic import (
    BaseModel, HttpUrl, validator
)


__all__ = [
    "RequestBase",
    "RequestSchemas",
    "DeleteCases",
    "BatchTestCaseRequest",
    "CasesRunRequest"
]


class RequestBase(BaseModel):
    method: str
    url: HttpUrl
    json_data: Union[Dict, None] = None
    form_data:  Union[Dict, None] = None
    headers: Union[Dict, None] = None
    content: Optional[Any] = None
    files: Optional[Any] = None
    params: Optional[Any] = None
    cookies: Optional[Any] = None
    timeout: Optional[Any] = None
    expected_result: Optional[Any] = None

    @validator('method', 'url')
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise Exception(f"{v} 不能为空")
        return v


class RequestSchemas(RequestBase):
    plan_id: Optional[int] = None


class DeleteCases(BaseModel):
    case_ids: List[int]

    @validator('case_ids')
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise Exception(f"{v} 不能为空")
        return v


class TestCaseRequest(BaseModel):
    case_ids: List[RequestBase]


class BatchTestCaseRequest(DeleteCases):
    plan_id: int = None


class CasesRunRequest(BaseModel):
    case_ids: List[int]
    plan_id: int = None

    @validator('case_ids')
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise Exception(f"{v} 不能为空")
        return v
