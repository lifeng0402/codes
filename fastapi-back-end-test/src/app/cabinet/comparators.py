#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: comparators.py
@时间: 2023/07/25 10:50:29
@说明: 
"""

import re
from typing import (
    Text, Any, Union
)


class Comparators:

    @staticmethod
    def equal(check_value: Any, expect_value: Any, message: Text = ""):
        assert check_value == expect_value, message

    @staticmethod
    def not_equal(check_value: Any, expect_value: Any, message: Text = ""):
        assert check_value != expect_value, message

    @staticmethod
    def string_equals(check_value: Text, expect_value: Any, message: Text = ""):
        assert str(check_value) == str(expect_value), message





comparators = Comparators

assert_result = getattr(comparators, "not_equal")

print(assert_result(1, 2))
