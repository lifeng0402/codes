#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 15:23
# @Author  : debugfeng
# @Site    : 
# @File    : logger.py
# @Software: PyCharm

import logging
from src.app import setting as st

__all_ = ["do_logger"]


class _Logger:

    def __init__(self):
        _datas = st.LOGGING_DATA

        self._logger = logging.getLogger()  # 日志收集器
        self._logger.setLevel(st.LEVEL_LOGGER)  # 设置日志级别

        # 日志输入渠道，输出到控制台及日志文件中
        _console_log = logging.StreamHandler()
        _write_file_log = logging.FileHandler(_datas["logging_path"], encoding='utf-8')  # 写入文件

        # 指定控制台日志文件的输出格式
        _console_log.setLevel(logging.DEBUG)
        _write_file_log.setLevel(logging.ERROR)

        # 显示控制台及日志文件里面的格式
        _console_output = logging.Formatter(_datas["console_formatters"])
        _file_output = logging.Formatter(_datas["file_formatters"])
        _console_log.setFormatter(_console_output)
        _write_file_log.setFormatter(_file_output)

        # 收集器对接输出渠道
        self._logger.addHandler(_console_log)
        self._logger.addHandler(_write_file_log)

    @property
    def get_logger(self):
        return self._logger


do_logger = _Logger().get_logger

if __name__ == '__main__':
    do_logger.info("eeee")
