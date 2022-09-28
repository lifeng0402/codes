#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/21 19:07
# @Author  : Lifeng
# @Site    : 
# @File    : databases.py
# @Software: PyCharm
import typing

from src.app import setting as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

__all__ = ["session_local", "database_commit", "Engine"]


class _Connect:
    # 定义一个变量
    _connect_ip = st.DATABASES["PRO"] if st.ENVIRONMENT else st.DATABASES["TEST"]
    _sqlalchemy_url = f"mysql+pymysql://root:123456@{_connect_ip}:3307/api_test?charset=utf8"
    engine = create_engine(_sqlalchemy_url, pool_pre_ping=True, encoding="utf-8", echo=True, future=True)
    # 创建一个持久对象，好处就是可以一次添加多个对象
    SessionLocals = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    # 定义一个ORM模型基类
    declarative_base(engine)


Engine = _Connect.engine


def session_local():
    db = _Connect.SessionLocals()
    try:
        yield db
    finally:
        db.close()


def database_commit(*, _session: typing.Any, _datas: typing.Any):
    # 添加用户数据
    _session.add(_datas)
    # 提交用户数据
    _session.commit()
    # # 刷新用户数据
    _session.refresh(_datas)
