#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: config.py
@时间: 2023/05/31 11:09:45
@说明: 
"""

import os
from typing import (
    Optional,
    Dict,
    Any,
    List
)
from pydantic import (
    BaseSettings,
    validator
)
from pathlib import Path
from src.app.cabinet.code_pydantic import DatabasesDsn


__all__ = [
    "settings"
]


class Settings(BaseSettings):

    SECRET: str
    ALGORITHM: str

    # Redis连接信息
    REDIS_SERVER: str
    REDIS_PORT: int
    REDIS_DB: int

    # 数据库连接信息
    MYSQL_SERVER: str
    MYSQL_PORT: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[DatabasesDsn] = None

    # validator是指一个用于验证数据是否符合规则的函数。
    # 它可以用于验证输入的数据是否为字符串、整数、浮点数等等，并在不符合规则时抛出相应的异常。

    @validator("SQLALCHEMY_DATABASE_URI")
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]):
        if isinstance(v, str):
            return v
        return DatabasesDsn.build(
            scheme="mysql+pymysql",
            user=values.get("MYSQL_USER"),
            password=values.get("MYSQL_PASSWORD"),
            host=values.get("MYSQL_SERVER"),
            port=values.get("MYSQL_PORT"),
            path=f'/{values.get("MYSQL_DB")}?charset=utf8'
        )


class SettingsDevd(Settings):
    # 开发环境读取配置
    class Config:
        case_sensitive = True
        env_file = Path(__file__).parent.parent.joinpath("dev.env")
        env_file_encoding = "utf-8"


# class SettingsProd(Settings):
#     # 预发布线上环境读取配置
#     class Config:
#         case_sensitive = True
#         env_file = "../dev.env"
#         env_file_encoding = "utf-8"


# _PY_ENV = os.getenv("PY_ENV", "DEV")
# settings = SettingsProd() if (_PY_ENV and _PY_ENV.isupper()) else SettingsDevd()
settings = SettingsDevd()
