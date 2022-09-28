#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 15:52
# @Author  : debugfeng
# @Site    : 
# @File    : cases_schemas.py
# @Software: PyCharm

from pydantic import validator
from typing import Union, Optional
from pydantic import BaseModel, HttpUrl
from src.app.handler.enum_fatcory import BodyType

__all__ = ["CaseDatas"]


class CaseDatas(BaseModel):
    name: str
    method: str
    url: HttpUrl
    headers: dict
    body_type: BodyType
    body: Optional[Union[str, dict]] = None
    params: Optional[Union[str, dict]] = None
    cookies: Optional[Union[str, dict]] = None

    @classmethod
    @validator('method', 'url', "headers")
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ValueError(f"{v} 不能为空")
        return v
