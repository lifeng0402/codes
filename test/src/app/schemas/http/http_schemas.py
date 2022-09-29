#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 17:27
# @Author  : debugfeng
# @Site    : 
# @File    : http_schemas.py
# @Software: PyCharm

from pydantic import validator
from typing import Union, Optional
from pydantic import BaseModel, HttpUrl
from src.app.enumeration.request_enum import BodyType

__all__ = ["HttpBody", "HttpBodySave"]


class HttpBody(BaseModel):
    method: str
    url: HttpUrl
    headers: dict
    body_type: BodyType
    body: Optional[Union[str, dict]] = None
    params: Optional[Union[str, dict]] = None
    cookies: Optional[Union[str, dict]] = None

    @classmethod
    @validator("method", "url", "headers")
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ValueError(f"{v} 不能为空")
        return v


class HttpBodySave(HttpBody):
    title: str
    actual: Optional[Union[str, dict]] = None
    expect: Optional[Union[str, dict]] = None

    @classmethod
    @validator("title", "method", "url", "headers")
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ValueError(f"{v} 不能为空")
        return v
