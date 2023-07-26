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


class Parser:

    def __init__(self):
        self._comparators = comparators

    def get_function_mapping(self, function_name: ty.Text) -> callable:
        """
        根据传入的函数名称,判断类中是否存在
        存在则执行, 不存在则抛异常。

        :param function_name: _description_
        :type function_name: ty.Text
        :return: _description_
        :rtype: callable
        """
        if not hasattr(self._comparators, function_name):
            raise

        return getattr(self._comparators, function_name)
