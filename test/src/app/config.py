#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 15:46
# @Author  : debugfeng
# @Site    :
# @File    : config.py
# @Software: PyCharm


from pydantic import BaseSettings

__all__ = [
    "settings"
]

# 从配置文件中读取信息


class Settings(BaseSettings):
    ENCRYPTION: str
    CRYPTCONTEXT: str
    ENVIRONMENT: bool
    DATABASE_URL: str
    REDIS_URL: str
    REDIS_PORT: int
    REDIS_DB: int

    # 指定配置文件
    class Config:
        env_file = ".env"


settings = Settings()

# print(settings.REDIS_PORT)
