#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: handle_params.py
@时间: 2023/07/21 18:55:50
@说明:
"""


import json
import jmespath
import typing as ty
from loguru import logger
from jmespath.exceptions import JMESPathError
from src.app.core.excpetions import ParamsError
from src.app.cabinet.enumerate import (
    Checkout, Extractors
)
from src.app.core.parser import Parser


def get_uniform_comparator(comparator: ty.Text):
    """


    :param comparator: _description_
    :type comparator: ty.Text
    :return: _description_
    :rtype: _type_
    """
    if comparator in ["eq", "equals", "equal"]:
        return "equal"
    elif comparator in ["lt", "less_than"]:
        return "less_than"
    else:
        return comparator


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

    assert_method = get_uniform_comparator(comparator)

    return {
        "check": check_item,
        "expect": expect_value,
        "assert": assert_method
    }


class ResponseBase:

    def __init__(self, response: ty.Union[ty.Any, ty.Dict]) -> None:
        self.resp = response
        self.validation_results: ty.Dict = {}

    def validator(self, validators: Checkout):
        """


        :param validators: _description_
        :type validators: Validators
        :raises ex: _description_
        """
        for items in validators:
            u_validator = uniform_validator(items)

            check_item = u_validator["check"]

            # if "$" in check_item:
            #     pass
            if check_item and isinstance(check_item, ty.Text):
                check_value = self._search_jmespath(check_item)
            else:
                check_value = check_item

            assert_method = u_validator["assert"]
            expect_item = u_validator["expect"]

            assert_func = Parser.get_function_mapping(assert_method)

            validate_msg = f"assert {check_item} {assert_method} {expect_item}"

            validator_dict = {
                "comparator": assert_method,
                "check": check_item,
                "expect": expect_item,
            }

            try:
                assert_func(check_value, expect_item)
                validator_dict["check_result"] = True
            except AssertionError as ex:
                validator_dict["check_result"] = False
                raise ex

            self.validation_results.update(validator_dict)

        return self.validation_results

    def extract(self, extractors: Extractors):
        """
        根据传入的表达式提取出参数并塞入到新字典

        :param extractors: 传参
        :type extractors: Extractors
        :return: 返回一个字典
        :rtype: dict
        """
        if not extractors:
            return {}

        extract_mapping = {}

        for key, field in extractors.items():
            field_value = self._search_jmespath(field)
            extract_mapping[key] = field_value

        return extract_mapping

    def _search_jmespath(self, extr: ty.Text):
        """
        根据表达式提取参数

        :param extr: 提取表达式
        :type extr: ty.Text
        :return: 返回一个列表
        :rtype: list
        """
        try:
            check_value = jmespath.search(extr, self.resp)
        except JMESPathError as ex:
            logger.error(ex)
            raise

        return check_value


def call_test(a: int, b: int):
    return a+b


if __name__ == "__main__":
    assert_func = getattr(object, "call_test")
    print(assert_func(1, 2))

    # response = {
    #     "id": 85856,
    #     "status_code": 200,
    #     "username": "user10",
    #     "list": [
    #         {
    #             "cc": 111,
    #             "gg": 222
    #         },
    #         {
    #             "dd": 333,
    #             "hh": 444
    #         }
    #     ]
    # }

    # results = [
    #     {
    #         "check": "status_code",
    #         "assert": "equal",
    #         "expect": 200
    #     },
    #     {
    #         "check": 201,
    #         "assert": "equal",
    #         "expect": 5552222
    #     }
    # ]

    # resp = ResponseBase(response)

    # results = resp.validator(results)

    # print(results)
