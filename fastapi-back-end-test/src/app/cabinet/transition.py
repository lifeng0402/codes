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
from src.app.excpetions.custom_json import DateTimeEncoder


class Transition:

    @staticmethod
    def proof_dict(data: ty.Any):
        """
        把json字符串转换成字典
        如非json字符串直接返回数据
        @param  :
        @return  :
        """
        try:
            # 判断值是否为真
            if not data:
                return data
            return json.loads(data)
        except json.decoder.JSONDecodeError:
            return data

    @staticmethod
    def proof_json(data: str, json_error: bool = False):
        """
        把字符串转成json数据
        如转换不成功则直接返回或者抛出错误提示
        @param  :
        @return  :
        """
        try:
            # 判断值是否为真
            if not data:
                return data
            return json.dumps(data, indent=4)
        except json.JSONDecodeError:
            if json_error:
                raise json.JSONDecodeError("请求参数非json类型")
            else:
                return data

    @staticmethod
    def proof_timestamp(data: ty.Dict):
        """
        对返回值中含未格式化的日期进行格式化操作
        @param  :
        @return  :
        """
        result = json.loads(
            json.dumps(
                data, ensure_ascii=False, cls=DateTimeEncoder
            )
        )
        return result
