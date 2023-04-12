#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: workes.py
@时间: 2023/04/12 08:28:20
@说明:
"""

from pydantic import AnyUrl


class MysqlDsn(AnyUrl):
    allowed_schemes = {
        'mysql+pymysql'
    }
    user_required = True


class ReadEnvConfig:

    @classmethod
    def redis_build(cls, *, host, port, db, **_kwargs: str,):
        return dict(
            host=host, port=port, db=db, **_kwargs
        )

    @classmethod
    def logging_build(
        cls, *, level, file_name, console_formatters, file_formatters, **_kwargs: str
    ):
        return dict(
            level=level, file_name=file_name,
            console_formatters=console_formatters,
            file_formatters=file_formatters, **_kwargs
        )

    @classmethod
    def fastapi_build(
        cls, *, app, host, port, log_level, **_kwargs: str
    ):
        return dict(
            app=app, host=host, port=port, log_level=log_level, **_kwargs
        )

    @classmethod
    def fastapi_text_build(
        cls, *, title, version, description, **_kwargs: str
    ):
        return dict(
            title=title, version=version, description=description, **_kwargs
        )
