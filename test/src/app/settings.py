#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 09:42
# @Author  : debugfeng
# @Site    : 
# @File    : settings.py
# @Software: PyCharm

from pathlib import Path

BASEDIR = Path(__file__).parent

# 日志存放目录及配置
COMMON_FORMATTERS = "运行日志：%(asctime)s [%(name)s:%(lineno)d] [%(module)s:%(funcName)s]: %(message)s"
LOGGING_DATA = {
    "logging_path": BASEDIR.joinpath("logs").joinpath("lms39first.log"),
    "console_formatters": COMMON_FORMATTERS,
    "file_formatters": f"{COMMON_FORMATTERS}- %(pathname)s"
}
