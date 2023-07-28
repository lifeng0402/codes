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
from src.app.core.excpetions import ParamsError

__all__ = [
    "Parser"
]


class Parser:

    @staticmethod
    def get_uniform_comparator(comparator: ty.Text):
        """
        判断所传断言参数是否符合要求
        符合则返回对应值

        :param comparator: _description_
        :type comparator: ty.Text
        :return: _description_
        :rtype: _type_
        """
        if comparator in ["eq", "equals", "equal"]:
            return "equal"
        elif comparator in ["lt", "less_than"]:
            return "less_than"
        elif comparator in ["neq", "not_equal"]:
            return "not_equal"
        else:
            return comparator

    @staticmethod
    def uniform_validator(validator):
        """
        判断字典中是否存在参数

        :param validator: 传参
        :type validator: ty.Dict
        :raises ParamsError: 抛出异常
        :raises ParamsError: 抛出异常
        :return: 返回一个字典
        :rtype: dict
        """
        if not isinstance(validator, dict):
            raise ParamsError(f"无效的验证 {validator}")

        if "check" in validator and "expect" in validator:
            check_item = validator["check"]
            expect_value = validator["expect"]

            if "assert" in validator:
                comparator = validator.get("assert")
            else:
                comparator = validator.get("comparator", "eq")
        else:
            raise ParamsError(f"无效的验证 {validator}")

        assert_method = Parser.get_uniform_comparator(comparator)

        return {
            "check": check_item,
            "expect": expect_value,
            "assert": assert_method
        }

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

        # 如果方法不存在则抛出异常
        if not hasattr(comparators, function_name):
            raise

        return getattr(comparators, function_name)
