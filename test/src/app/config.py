#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 15:46
# @Author  : debugfeng
# @Site    : 
# @File    : config.py
# @Software: PyCharm

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings
from pathlib import Path


__all__ = ["ReadConfig"]


class ReadConfig:
    _config = Config(".env")

    @classmethod
    def value(cls, *, variable: str):
        """
        读取配置文件中的数据，返回数据
        :param variable:
        :return:
        """
        return cls._config(variable)

    @classmethod
    def value_array(cls, *, variable: str):
        """
        读取配置文件中的数据，返回列表
        :param variable:
        :return:
        """
        variable = cls.value(variable=variable)
        return list(CommaSeparatedStrings(variable))


if __name__ == '__main__':
    print(ReadConfig.value_array(variable="ENCRYPTION"))


