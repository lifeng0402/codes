#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 15:23
# @Author  : debugfeng
# @Site    : 
# @File    : logger.py
# @Software: PyCharm

import logging
from src.app import settings

__all_ = [
    "do_logger"
]


class Logger:

    def __init__(self):
        _datas = settings.LOGGING_DATA

        self._logger = logging.getLogger()  # 日志收集器
        self._logger.setLevel(logging.INFO)  # 设置日志级别

        # 日志输入渠道，输出到控制台及日志文件中
        console_log = logging.StreamHandler()
        write_file_log = logging.FileHandler(_datas["logging_path"], encoding='utf-8')  # 写入文件

        # 指定控制台日志文件的输出格式
        console_log.setLevel(logging.DEBUG)
        write_file_log.setLevel(logging.ERROR)

        # 显示控制台及日志文件里面的格式
        console_output = logging.Formatter(_datas["console_formatters"])
        file_output = logging.Formatter(_datas["file_formatters"])
        console_log.setFormatter(console_output)
        write_file_log.setFormatter(file_output)

        # 收集器对接输出渠道
        self._logger.addHandler(console_log)
        self._logger.addHandler(write_file_log)

    @property
    def get_logger(self):
        return self._logger


do_logger = Logger().get_logger
