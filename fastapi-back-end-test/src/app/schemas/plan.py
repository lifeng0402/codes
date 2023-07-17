#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: plan_schemas.py
@时间: 2023/06/20 18:56:48
@说明: 
"""

from typing import (
    Any,
    Optional
)
from pydantic import (
    BaseModel, validator
)
from src.app.cabinet.enumerate import Environment

__all__ = [
    "PlanSchemas"
]


class PlanSchemas(BaseModel):
    title: str
    environment: Environment = Environment.test.value
    description: Optional[Any] = None

    @validator('title')
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise Exception(f"{v} 不能为空")
        return v
