#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 18:16
# @Author  : debugfeng
# @Site    : 
# @File    : enum_fatcory.py
# @Software: PyCharm


from enum import IntEnum

__all__ = ["BodyType"]


class BodyType(IntEnum):
    """
    枚举类型
    """
    none = 0
    json = 1
    form_data = 2
    form_urlencoded = 3
    binary = 4
    graphQL = 5
