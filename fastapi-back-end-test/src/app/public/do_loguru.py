#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: do_logging.py
@时间: 2023/07/17 20:40:40
@说明: 
"""


import os
import time
from loguru import logger
from functools import wraps
from pathlib import Path


class DoLoguru:
    def __init__(self) -> None:

        self._logger = logger.add(colorize=True)

    @property
    def logs(self):
        return self._logger


# do_log = DoLoguru().logs
