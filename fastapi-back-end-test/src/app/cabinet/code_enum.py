#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: code_enum.py
@时间: 2023/06/10 17:26:19
@说明: 
"""

from enum import Enum, unique

__all__ = [
    "RequestBody"
]


@unique
class RequestBody(Enum):
    none: int = 0
    raw: int = 1
    graphql: int = 2
    form_data: int = 3
    binary: int = 4
    x_www_form_urlencoded: int = 5


@unique
class JsonRaw(Enum):
    pass
