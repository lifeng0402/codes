#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 15:52
# @Author  : debugfeng
# @Site    : 
# @File    : cases_schemas.py
# @Software: PyCharm

from typing import Union
from pydantic import validator
from pydantic import BaseModel
from src.app.enumeration.request_enum import BodyType

__all__ = ["CaseDatas"]


class CaseDatas(BaseModel):
    case_id: Union[int, list[int]]

    @classmethod
    @validator("case_id")
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ValueError(f"{v} 不能为空")
        return v
