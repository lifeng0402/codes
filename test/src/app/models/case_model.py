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
    case_name = Column(String(20), unique=True, nullable=False)
    project_leader = Column(String(10), nullable=False)
    project_description = Column(String(500), nullable=False)
    is_active = Column(Boolean, default=True)
    created_time = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated_time = Column(TIMESTAMP, nullable=False, default=datetime.now())
