#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: session.py
@时间: 2023/05/31 11:28:53
@说明:
"""


from sqlalchemy.orm import Session
from src.app.core.database.session_context import SessionContextManager

__all__ = [
    "session",
    "session_commit",
]


async def session():
    with SessionContextManager() as db:
        yield db


def session_commit(db: Session, *, datas):
    # 往数据库添加数据
    db.add(datas)
    # 往数据库提交数据
    db.commit()
    # 刷新提交的数据
    db.refresh(datas)
    return datas
