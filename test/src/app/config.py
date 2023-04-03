#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 15:46
# @Author  : debugfeng
# @Site    :
# @File    : config.py
# @Software: PyCharm


from starlette.config import Config
from starlette.datastructures import (
    CommaSeparatedStrings, Secret
)


_config = Config(".env")

# token加密方式
SECRET_KEY = _config('SECRET_KEY', cast=Secret)
# 获取程序运行环境
ENVIRONMENT = _config("ENVIRONMENT", cast=bool, default=False)
# 获取redis数据库URL
REDIS_URL, R_ = _config('REDIS_HOST_URL', cast=CommaSeparatedStrings)
# 获取数据库URL
DATABASE_URL, D_ = _config('DATABASE_URL', cast=CommaSeparatedStrings)

# 判断环境返回对应数据连接
if ENVIRONMENT:
    DATABASE_URL, REDIS_URL = D_, R_


print(REDIS_URL)
