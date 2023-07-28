#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: excpetions.py
@时间: 2023/07/26 11:38:37
@说明: 
"""

import json
import datetime


class MyBaseError(Exception):
    pass


class ParamsError(MyBaseError):
    pass


class DebugTestException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# 继承 json.JSONEncoder 类，并添加对 datetime 类型的支持
class DateTimeEncoder(json.JSONEncoder):
    def default(self, value):
        if isinstance(value, datetime.datetime):
            return value.strftime('%Y-%m-%d %H:%M:%S')
        return json.JSONEncoder.default(self, value)


# 自定义 json 编码器
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)
