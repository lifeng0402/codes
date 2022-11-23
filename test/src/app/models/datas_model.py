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
    title = Column(String(20), unique=True, nullable=False, comment="名称")
    method = Column(String(10), nullable=False, comment="请求方式")
    url = Column(String(200), nullable=False, comment="请求的URL")
    headers = Column(TEXT, nullable=False, comment="请求的头部信息")
    body_type = Column(INT, nullable=False, comment="请求类型，区分json、form-data等")
    params = Column(TEXT, comment="请求参数-params")
    body = Column(TEXT, comment="请求参数-body体")
    cookies = Column(TEXT, comment="cookies")
    actual = Column(TEXT, comment="断言使用-接口的实际结果")
    expect = Column(TEXT, comment="断言使用-接口的预期结果")
    comparison = Column(TEXT, comment="断言比较符号")
    is_active = Column(Boolean, default=True, comment="是否被删除")
    created_time = Column(TIMESTAMP, nullable=False, default=datetime.now(), comment="创建时间")
    updated_time = Column(TIMESTAMP, nullable=False, default=datetime.now(), comment="更新时间")
