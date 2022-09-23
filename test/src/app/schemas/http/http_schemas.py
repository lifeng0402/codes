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
from src.app.handler.enum_fatcory import BodyType

__all__ = ["HttpBody"]


class HttpBody(BaseModel):
    method: str
    url: HttpUrl
    headers: dict
    body: Optional[Union[str, dict]] = None
    body_type: BodyType = BodyType.none

    @classmethod
    @validator('method', 'url', "headers")
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ValueError("不能为空")
        return v
