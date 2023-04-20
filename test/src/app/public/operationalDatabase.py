#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: operationalDatabase.py
@时间: 2023/04/06 10:40:26
@说明: 
"""

import sqlalchemy
from typing import Any
from src.config import Confing
from sqlalchemy.orm import sessionmaker


# DATABASE_URL = "mysql+pymysql://root:123456@10.10.12.199:3307/api_test"
# engine = sqlalchemy.create_engine(DATABASE_URL, pool_pre_ping=True)
# # 创建一个持久对象，好处就是可以一次添加多个对象
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def operDatabase():
    """
    数据库连接方法
    @param  :
    @return  :
    """
    # 创建一个持久对象
    db = sessionmaker(
        autocommit=False, autoflush=False,
        # 连接数据库
        bind=sqlalchemy.create_engine(
            url=Confing.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True
        )
    )
    # 初始化对象
    session = db()
    try:
        yield session
    finally:
        session.close()


def databaseCommit(*, _session: Any, _datas: Any):
    """
    提交指定数据
    :param _session:
    :param _datas:
    :return:
    """
    # 添加用户数据
    _session.add(_datas)
    # 提交用户数据
    _session.commit()
    # # 刷新用户数据
    _session.refresh(_datas)
    return _datas
