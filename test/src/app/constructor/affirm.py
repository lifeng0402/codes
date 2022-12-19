#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/30 15:57
# @Author  : debugfeng
# @Site    : 
# @File    : affirm.py
# @Software: PyCharm

import traceback
import typing
from fastapi import status


def self_equal(*, expect: typing.Any, actual: typing.Any, msg: str = ""):
    try:
        assert expect == actual, msg
    except AssertionError:
        traceback.print_exc()


def self_not_equal(*, expect: typing.Any, actual: typing.Any, msg: str = ""):
    try:
        assert expect != actual, msg
    except AssertionError:
        traceback.print_exc()


def self_include(*, expect: typing.Any, actual: typing.Any, msg: str = ""):
    try:
        assert expect in actual, msg
    except AssertionError:
        traceback.print_exc()



def self_main(*, comparison: str, expect: typing.Any, response: typing.Any):
    match comparison:
        case "==":
            self_equal(expect=expect, actual=response)
        case "!=":
            self_not_equal(expect=expect, actual=response)
        case "in":
            self_include(expect=expect, actual=response)
        case _:
            pass
