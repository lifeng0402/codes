#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 15:46
# @Author  : debugfeng
# @Site    :
# @File    : config.py
# @Software: PyCharm


from pydantic import BaseSettings


class Settings(BaseSettings):
    encryption: str
    environment: bool
    database_url: str
    redis_url: str

    class Config:
        env_file = "test.env"


class TestSettings(BaseSettings):
    encryption: str
    environment: bool
    database_url: str
    redis_url: str

    class Config:
        env_file = "test.env"

class TestSettings(BaseSettings):
    encryption: str
    environment: bool
    database_url: str
    redis_url: str

    class Config:
        env_file = "test.env"


print(TestSettings())
