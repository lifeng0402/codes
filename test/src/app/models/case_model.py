#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 15:42
# @Author  : debugfeng
# @Site    : 
# @File    : case_model.py
# @Software: PyCharm

from src.app.models import *

__all__ = ["Cases"]

# 定义一个ORM模型基类
Base = declarative_base(Engine)


class Cases(Base):
    __tablename__ = "cases"

    # 用例表
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True, nullable=False, comment="用例名称")
    datas = Column(TEXT, nullable=False, comment="测试数据，请求方式、请求体、请求头")
    actual = Column(TEXT, comment="断言-实际结果")
    expect = Column(TEXT, comment="断言-预期结果")
    comparison = Column(TEXT, comment="断言符号")
    is_success = Column(Boolean, comment="是否执行成功")
    is_error = Column(Boolean, comment="是否错误")
    exception = Column(TEXT, comment="报错异常捕获")
    is_active = Column(Boolean, default=False, comment="是否被删除")
    created_time = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated_time = Column(TIMESTAMP, nullable=False, default=datetime.now())
