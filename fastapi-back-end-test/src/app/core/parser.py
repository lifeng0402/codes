#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: parser.py
@时间: 2023/07/26 20:49:25
@说明: 
"""

import typing as ty
from src.app.cabinet.comparators import comparators

__all__ = [
    "Parser"
]


class Parser:

    @staticmethod
    def get_function_mapping(function_name: ty.Text) -> callable:
        """
        根据传入的函数名称,判断类中是否存在
        存在则执行, 不存在则抛异常。

        :param function_name: _description_
        :type function_name: ty.Text
        :return: _description_
        :rtype: callable
        """
        if not hasattr(comparators, function_name):
            raise

        return getattr(comparators, function_name)
