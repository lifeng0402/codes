#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: cases_schemas.py
@时间: 2023/06/10 16:56:08
@说明: 
"""

import typing as ty
from dataclasses import dataclass
from pydantic import (
    BaseModel,
    HttpUrl
)


@dataclass
class RequestSchemas(BaseModel):
    method: str
    url: HttpUrl
    headers: ty.Dict
    params: ty.Any
    body: ty.Dict
