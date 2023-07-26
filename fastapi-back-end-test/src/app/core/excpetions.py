#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: excpetions.py
@时间: 2023/07/26 11:38:37
@说明: 
"""


class MyBaseError(Exception):
    pass


class ParamsError(MyBaseError):
    pass


class DebugTestException(MyBaseError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
