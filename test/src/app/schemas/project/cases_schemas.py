#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 15:52
# @Author  : debugfeng
# @Site    : 
# @File    : cases_schemas.py
# @Software: PyCharm

from typing import Union, Optional
from pydantic import validator
from pydantic import BaseModel, HttpUrl
from src.app.enumeration.request_enum import BodyType

__all__ = ["CaseDatas", "CaseAdd"]


class CaseDatas(BaseModel):
    case_id: list[int]

    @classmethod
    @validator("case_id")
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ValueError(f"{v} 不能为空")
        return v


class CaseAdd(BaseModel):
    name: str
    method: str
    url: HttpUrl
    headers: dict
    body_type: BodyType
    body: Optional[Union[str, dict]] = None
    params: Optional[Union[str, dict]] = None
    cookies: Optional[Union[str, dict]] = None
    comparison: Optional[Union[str, dict]] = None
    actual: Optional[Union[str, dict]] = None
    expect: Optional[Union[str, dict]] = None

    @classmethod
    @validator("case_name", "method", "url", "headers", "body_type")
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ValueError(f"{v} 不能为空")
        return v
