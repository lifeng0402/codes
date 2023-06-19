#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: json_datatime.py
@时间: 2023/06/19 18:50:30
@说明: 
"""


import json
import datetime

# 继承 json.JSONEncoder 类，并添加对 datetime 类型的支持

__all__ = [
    "DateTimeEncoder"
]


class DateTimeEncoder(json.JSONEncoder):
    def default(self, value):
        if isinstance(value, datetime.datetime):
            return value.strftime('%Y-%m-%d %H:%M:%S')
        return json.JSONEncoder.default(self, value)


# 将数据序列化为 JSON 格式
# data = {'timestamp': datetime.datetime.now(), 'message': 'hello, world'}
# json.dumps(data, cls=DateTimeEncoder)
# print(json.dumps(data, cls=DateTimeEncoder))
