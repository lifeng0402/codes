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
    "BodyType",
    "Environment"
]


@unique
class BodyType(Enum):
    none: int = 0
    raw: int = 1
    graphql: int = 2
    form_data: int = 3
    binary: int = 4
    x_form_url: int = 5


@unique
class Environment(Enum):
    test: int = 0
    pre: int = 1
    pro: int = 2


@unique
class LoginMethodEnum(Enum):
    username: int = 0
    mobile: int = 1
    mailbox: int = 2
