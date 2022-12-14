#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 09:39
# @Author  : debugfeng
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm

from . import global_settings

__all__ = ["setting"]


class _Settings:

    def __init__(self):
        for name in dir(global_settings):
            # 判断是不是大写
            if name.isupper():
                # 读取到值后赋值给value
                value = getattr(global_settings, name)
                # 再把value成name的值
                setattr(self, name, value)


# 实例化一个对象
setting = _Settings()
