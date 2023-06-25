#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: datetime_excpetions.py
@时间: 2023/06/20 08:13:28
@说明: 
"""

import json
import datetime


__all__ = [
    "DateTimeEncoder",
    "CustomJSONEncoder"
]

# 继承 json.JSONEncoder 类，并添加对 datetime 类型的支持
class DateTimeEncoder(json.JSONEncoder):
    def default(self, value):
        if isinstance(value, datetime.datetime):
            return value.strftime('%Y-%m-%d %H:%M:%S')
        return json.JSONEncoder.default(self, value)


# 自定义 json 编码器
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, dict):
            return json.dumps(obj, ensure_ascii=False)
        return json.JSONEncoder.default(self, obj)


# 将数据序列化为 JSON 格式
# data = {'timestamp': datetime.datetime.now(), 'message': 'hello, world'}
# json.dumps(data, cls=DateTimeEncoder)
# print(json.dumps(data, cls=DateTimeEncoder))
