#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: cases_schemas.py
@时间: 2023/06/10 16:56:08
@说明: 
"""

import typing
from typing import (
    Optional,
    Any
)
from dataclasses import dataclass
from pydantic import (
    BaseModel,
    HttpUrl
)

__all__ = [
    "RequestSchemas"
]


class RequestSchemas(BaseModel):
    method: str
    url: HttpUrl
    content: Optional[Any] = None
    data: Optional[Any] = None
    files: Optional[Any] = None
    json_data: Optional[Any] = None   # json传参
    params: Optional[Any] = None
    headers: Optional[Any] = None
    cookies: Optional[Any] = None
    auth: Optional[Any] = None
    follow_redirects: Optional[Any] = None
    timeout: Optional[Any] = None
    extensions: Optional[Any] = None
