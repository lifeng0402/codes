#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: session.py
@时间: 2023/05/31 11:28:53
@说明:
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.conf.config import settings

__all__ = [
    "session"
]


class Csession:

    def __init__(self) -> None:
        # 创建一个持久对象
        self._db = sessionmaker(
            autocommit=False, autoflush=False,
            # 连接数据库
            bind=create_engine(
                url=settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True
            )
        )

    def session(self):
        # 初始化对象
        session = self._db()
        try:
            yield session
        except Exception as exc:
            raise exc
        finally:
            session.close()


session = Csession().session
