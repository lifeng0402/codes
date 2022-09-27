#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/21 19:07
# @Author  : Lifeng
# @Site    : 
# @File    : databases.py
# @Software: PyCharm

from src.app import setting as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

__all__ = ["session_local", "Base"]


class _Connect:
    # 定义一个变量
    _connect_ip = st.DATABASES["PRO"] if st.ENVIRONMENT else st.DATABASES["TEST"]
    _sqlalchemy_url = f"mysql+pymysql://root:123456@{_connect_ip}:3307/api_test?charset=utf8"
    engine = create_engine(_sqlalchemy_url, pool_pre_ping=True, encoding="utf-8", echo=True, future=True)
    # 创建一个持久对象，好处就是可以一次添加多个对象
    SessionLocals = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    # 定义一个ORM模型基类
    Base = declarative_base(engine)


Base = _Connect.Base
Engine = _Connect.engine


def session_local():
    db = _Connect.SessionLocals()
    try:
        yield db
    finally:
        db.close()
