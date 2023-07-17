#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: data_transition.py
@时间: 2023/06/20 18:49:21
@说明: 
"""

import json
import datetime
import typing as ty
from src.app.excpetions.debug_test import DateTimeEncoder


class Transition:

    @staticmethod
    def proof_dict(data: ty.Dict, condition: str = None):
        """
        遍历字典,如果value值为真就赋值为空字符串,否则就保留原value
        condition条件为真则删除指定key
        最后直接返回处理好的字典
        @param  :
        @return  :
        """
        handled_dict = dict()

        for key, value in data.items():

            handled_dict[key] = "" if value is None else value

        if condition:
            del handled_dict[condition]

        return handled_dict

    @staticmethod
    def proof_timestamp(data: ty.Dict):
        """
        对返回值中含未格式化的日期进行格式化操作
        @param  :
        @return  :
        """
        result = json.loads(
            json.dumps(data, ensure_ascii=False, cls=DateTimeEncoder)
        )
        return result
