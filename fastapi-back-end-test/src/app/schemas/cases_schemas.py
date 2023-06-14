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
    Union,
    Mapping
)
from pydantic import (
    BaseModel, HttpUrl
)
from src.app.cabinet.code_enum import RequestBody

__all__ = [
    "RequestSchemas",
    "BodySchemas"
]


class RequestSchemas(BaseModel):
    method: str
    url: HttpUrl
    content: Optional[Any] = None
    data: Optional[Any] = None
    files: Optional[Any] = None
    json_data: Optional[Any] = None
    params: Optional[Any] = None
    headers: Optional[Any] = None
    cookies: Optional[Any] = None
    auth: Optional[Any] = None
    follow_redirects: Optional[Any] = None
    timeout: Optional[Any] = None
    extensions: Optional[Any] = None


class BodySchemas(BaseModel):
    body: RequestSchemas
    expected_result: Optional[Mapping[str, Any]] = None
