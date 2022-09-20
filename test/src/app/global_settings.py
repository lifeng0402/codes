#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 09:42
# @Author  : debugfeng
# @Site    : 
# @File    : global_settings.py
# @Software: PyCharm

from pathlib import Path

# 项目根路径
basedir = Path(__file__).parent

# 区分生产和测试环境
ENVIRONMENT = False

# 数据连接配置
DATABASES = {
    "TEST": "192.168.150.130", "PRO": "192.168.150.130"
}

# redis连接配置
REDIS_DATABASES = {
    "TEST": "192.168.150.130", "PRO": "192.168.150.130"
}

# 日志存放目录、格式化及日志级别配置
LEVEL_LOGGER = "INFO"
_formatter = "运行日志：%(asctime)s [%(name)s:%(lineno)d] [%(module)s:%(funcName)s]: %(message)s"
LOGGING_DATA = {
    "logging_path": basedir.joinpath("logs").joinpath("lms39first.log"),
    "console_formatters": _formatter,
    "file_formatters": f"{_formatter}- %(pathname)s"
}
