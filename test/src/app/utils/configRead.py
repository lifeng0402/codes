#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: configRead.py
@时间: 2023/04/12 08:28:20
@说明:
"""

from pydantic import AnyUrl

__all__ = [
    "MysqlDsn",
    "ReadEnvConfig"
]


class MysqlDsn(AnyUrl):
    """
    返回MySQL连接数据
    @param  :
    @return  :
    """
    allowed_schemes = {
        'mysql+pymysql'
    }
    user_required = True


class ReadEnvConfig:

    @classmethod
    def redis_build(cls, *, host, port, db, **_kwargs: str,):
        """
        返回字典形式的Redis连接数据
        @param  :
        @return  :
        """
        return dict(
            host=host, port=port, db=db, **_kwargs
        )

    @classmethod
    def logging_build(
        cls, *, level, file_name, console_formatters, file_formatters, **_kwargs: str
    ):
        """
        返回字典形式的Logging日志配置数据
        @param  :
        @return  :
        """
        return dict(
            level=level, file_name=file_name,
            console_formatters=console_formatters,
            file_formatters=file_formatters, **_kwargs
        )

    @classmethod
    def expire_build(cls, *, key, algorithm, expire_day):
        """
        返回元组形式的Token加密算法及过期天数
        @param  :
        @return  :
        """
        return (key, algorithm, expire_day)

    @classmethod
    def encryption_build(
        cls, *, encryption_sha, encryption_md5, encryption_dsc
    ):
        """
        返回元组形式的Token加密方式
        @param  :
        @return  :
        """
        return (
            encryption_sha, encryption_md5, encryption_dsc,
        )

    @classmethod
    def fastapi_build(
        cls, *, app, host, port, log_level, **_kwargs: str
    ):
        """
        返回字段形式的服务启动配置数据
        @param  :
        @return  :
        """
        return dict(
            app=app, host=host, port=port, log_level=log_level, **_kwargs
        )

    @classmethod
    def fastapi_text_build(
        cls, *, title, version, description, **_kwargs: str
    ):
        """
        返回字典形式的服务文本配置数据
        @param  :
        @return  :
        """
        return dict(
            title=title, version=version, description=description, **_kwargs
        )
