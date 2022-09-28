#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/26 09:36
# @Author  : debugfeng
# @Site    : 
# @File    : datas_model.py
# @Software: PyCharm

from src.app.models import *

__all__ = ["Datas"]

# 定义一个ORM模型基类
Base = declarative_base(Engine)


class Datas(Base):
    __tablename__ = "datas"

    id = Column(Integer, primary_key=True)
    title = Column(String(20), unique=True, nullable=False)
    method = Column(String(10), nullable=False)
    url = Column(String(200), nullable=False)
    headers = Column(String(200), nullable=False)
    body_type = Column(INT, nullable=False)
    params = Column(String(50))
    body = Column(String(200))
    cookies = Column(String(200))
    is_active = Column(Boolean, default=True)
    created_time = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated_time = Column(TIMESTAMP, nullable=False, default=datetime.now())

