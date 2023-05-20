#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/9 10:10
# @Author  : debugfeng
# @Site    :
# @File    : report_model.py
# @Software: PyCharm

from src.app.models import *

__all__ = ["Reposts"]

Base = declarative_base()


class Reposts(Base):
    __tablename__ = "reports"

    # 测试报告表
    id = Column(Integer, primary_key=True)
    report_datas = Column(TEXT, nullable=False, comment="测试报告数据")
    is_active = Column(Boolean, default=False, comment="是否被删除")
    created_time = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated_time = Column(TIMESTAMP, nullable=False, default=datetime.now())
