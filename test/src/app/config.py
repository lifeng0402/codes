#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 15:46
# @Author  : debugfeng
# @Site    :
# @File    : config.py
# @Software: PyCharm


from pathlib import Path
from typing import Optional, Dict, Any
from pydantic import BaseSettings, validator
from src.app.utils.workes import MysqlDsn, ReadEnvConfig

__all__ = [
    "settings"
]

# 从配置文件中读取信息


class Settings(BaseSettings):
    ENVIRONMENT: bool = False
    ENCRYPTION: tuple = ("123789&^%$abcdefg", "HS256", 3)
    CRYPTCONTEXT: tuple = ("sha256_crypt", "md5_crypt", "des_crypt")

    # 数据库连接地址
    MYSQL_SERVER: str
    MYSQL_PORT: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[MysqlDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def _assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return MysqlDsn.build(
            scheme="mysql+pymysql",
            user=values.get("MYSQL_USER"),
            password=values.get("MYSQL_PASSWORD"),
            host=values.get("MYSQL_SERVER"),
            port=values.get("MYSQL_PORT"),
            path=f"/{values.get('MYSQL_DB') or ''}",
        )

    # Redis连接地址
    REDIS_SERVER: str
    REDIS_PORT: str
    REDIS_DB: str
    REDIS_DATABASE_URI: Optional[Dict] = None

    @validator("REDIS_DATABASE_URI", pre=True)
    def _assemble_redis_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v

        return ReadEnvConfig.redis_build(
            host=values.get("REDIS_SERVER"),
            port=values.get("REDIS_PORT"),
            db=values.get('REDIS_DB'),
        )

    # 日志配置信息
    LEVEL_LOGGER: str
    LOGGING_FILE_NAME: str
    CONSOLE_FORMATTERS: str
    FILE_FORMATTERS: str
    LOGGING_DATA_DICT: Optional[Dict] = None

    @validator("LOGGING_DATA_DICT", pre=True)
    def _assemble_logging_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v

        return ReadEnvConfig.logging_build(
            level=values.get("LEVEL_LOGGER"),
            file_name=values.get("LOGGING_FILE_NAME"),
            console_formatters=values.get('CONSOLE_FORMATTERS'),
            file_formatters=values.get('FILE_FORMATTERS'),
        )

    # Fastapi服务启动配置信息
    SERVER_APP: str
    SERVER_HOST: str
    SERVER_PORT: str
    SERVER_LOG_LEVEL: str
    FASTAPI_DATA_DICT: Optional[Dict] = None

    @validator("FASTAPI_DATA_DICT", pre=True)
    def _assemble_fastapi_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v

        return ReadEnvConfig.fastapi_build(
            app=values.get("SERVER_APP"),
            host=values.get("SERVER_HOST"),
            port=values.get('SERVER_PORT'),
            log_level=values.get('SERVER_LOG_LEVEL'),
        )

    # Fastapi服务文本配置信息
    SERVER_TITLE: str
    SERVER_VERSION: str
    SERVER_DESCRIPTION: str
    FASTAPI_TEXT_DICT: Optional[Dict] = None

    @validator("FASTAPI_TEXT_DICT", pre=True)
    def _assemble_fastapi_text_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v

        return ReadEnvConfig.fastapi_text_build(
            title=values.get("SERVER_TITLE"),
            version=values.get("SERVER_VERSION"),
            description=values.get('SERVER_DESCRIPTION'),
        )

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


settings = Settings()


print(settings.FASTAPI_DATA_DICT)
