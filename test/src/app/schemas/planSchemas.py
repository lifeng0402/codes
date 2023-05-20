#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/18 18:21
# @Author  : debugfeng
# @Site    : 
# @File    : plan_schemas.py
# @Software: PyCharm
import typing

from pydantic import validator
from pydantic import BaseModel

__all__ = ["PlanAdd"]


class PlanAdd(BaseModel):
    name: str
    principal: str

    @classmethod
    @validator("name", "principal")
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ValueError(f"{v} 不能为空")
        return v


class PlanUpdate(PlanAdd):
    plan_id: int

    @classmethod
    @validator("plan_id")
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ValueError(f"{v} 不能为空")
        return v


class PlanData(BaseModel):
    case_id: typing.List[int]

    @classmethod
    @validator("plan_id")
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ValueError(f"{v} 不能为空")
        return v
