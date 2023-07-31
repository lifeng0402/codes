#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: handle_params.py
@时间: 2023/07/21 18:55:50
@说明:
"""


import jmespath
import typing as ty
from loguru import logger
from jmespath.exceptions import JMESPathError
from src.app.cabinet.enumerate import (
    Checkout, Extractors, Resp
)
from src.app.core.parser import Parser


__all__ = [
    "ResponseBase"
]


class ResponseBase:

    def __init__(self, resp: Resp) -> None:
        self.resp = resp
        self.validation_results: dict = {}

    def validator(self, validators: Checkout):
        """
        提取返回值值执行断言操作

        :param validators: _description_
        :type validators: Validators
        :raises ex: _description_
        """
        for items in validators:
            u_validator = Parser.uniform_validator(items)

            check_item = u_validator["check"]

            # if "$" in check_item:
            #     pass
            if check_item and isinstance(check_item, ty.Text):
                check_value = self._search_jmespath(check_item)
            else:
                check_value = check_item

            assert_method = u_validator["assert"]
            expect_value = u_validator["expect"]

            assert_func = Parser.get_function_mapping(assert_method)

            validate_msg = f"assert {check_value} {assert_method} {expect_value}"

            validator_dict = {
                "comparator": assert_method,
                "check_item": check_item,
                "check_value": check_value,
                "expect": expect_value,
            }

            # 判断参数如果是整型就转成字符串
            check_value = str(check_value) if isinstance(
                check_value, int) else check_value

            try:
                # 执行断言
                assert_func(check_value, expect_value)
                validator_dict["check_status"] = True
                validator_dict["message"] = "断言成功..."
            except AssertionError as ex:
                validator_dict["check_status"] = False
                validator_dict["message"] = f"断言失败..."
                logger.error(f"{validate_msg}/n{ex.args}")

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
        extract_mapping = {}

        if not extractors:
            return extract_mapping

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


if __name__ == "__main__":
    response = {
        "id": 85856,
        "status_code": 200,
        "username": "user10",
        "list": [
            {
                "cc": 111,
                "gg": 222
            },
            {
                "dd": 333,
                "hh": 444
            }
        ]
    }

    results = {
        "method": "GET",
        "url": "{{lms3}}/manager/index/index/list",
        "headers": {
            "token": "2fa575e61ccf5fd7e47d233083d9a6ea",
            "content_type": "application/json"
        },
        "json_data": {
            "a": 1,
            "b": 2
        },
        "extract": {
            "token": "username"
        },
        "checkout": [
            {
                "check": "Response.status_code",
                "assert": "equal",
                "expect": 200
            },
            {
                "check": "Response.status_code",
                "assert": "equal",
                "expect": 200
            }
        ]
    }

    resp = ResponseBase(response)

    results = resp.extract(results["extract"])

    print(results)
