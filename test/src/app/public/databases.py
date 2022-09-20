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

__all__ = ["DATABASES", "CONNECTDB"]


class DATABASES:
    _CONNECT_IP = st.DATABASES["PRO"] if st.ENVIRONMENT else st.DATABASES["TEST"]
    # 定义一个变量
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://root:123456@{_CONNECT_IP}:3307/api_test"
    # 创建一个连接
    ENGINE = create_engine(
        # echo=True参数表示连接发出的 SQL 将被记录到标准输出，future=True是为了确保我们使用最新的风格的API
        SQLALCHEMY_DATABASE_URL + "?charset=utf8",
        pool_pre_ping=True, encoding="utf-8", echo=True, future=True
    )
    # 创建一个持久对象，好处就是可以一次添加多个对象
    SESSIONLOCAL = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)


class CONNECTDB:
    def __init__(self, *, var):
        self._db = var

    def __enter__(self):
        return self._db

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._db.close()
