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
)
from pydantic import (
    BaseModel, HttpUrl, validator
)
from src.app.cabinet.code_enum import RequestBody

__all__ = [
    "RequestSchemas"
]


class RequestSchemas(BaseModel):
    method: str
    url: HttpUrl
    body_type: RequestBody = RequestBody.none.value
    content: Optional[Any] = None
    body: Optional[Any] = None
    files: Optional[Any] = None
    params: Optional[Any] = None
    headers: Optional[Any] = None
    cookies: Optional[Any] = None
    timeout: Optional[Any] = None
    expected_result: Optional[Any] = None
    plan_id: Optional[int] = None

    @validator('method', 'url')
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise Exception(f"{v} 不能为空")
        return v
