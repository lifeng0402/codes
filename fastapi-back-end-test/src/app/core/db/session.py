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


class SessionContextManager:
    def __init__(self) -> None:
        # 创建一个持久对象
        db_session = sessionmaker(
            autocommit=False, autoflush=False,
            # 连接数据库
            bind=create_engine(
                url=settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True
            )
        )
        # 新建一个session对象
        self._db = db_session()

    def __enter__(self):
        return self._db

    def __exit__(self, exc_type, exc_value, traceback):
        return self._db.close()


async def session():
    with SessionContextManager() as db:
        yield db


