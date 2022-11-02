#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 15:33
# @Author  : debugfeng
# @Site    : 
# @File    : project_model.py
# @Software: PyCharm

from src.app.models import *

__all__ = ["Projects"]

# 定义一个ORM模型基类
Base = declarative_base(Engine)


class Projects(Base):
    __tablename__ = "projects"

    # 项目信息表
    id = Column(Integer, primary_key=True)
    project_name = Column(String(20), unique=True, nullable=False, comment="项目名称")
    project_picture = Column(String(100), nullable=False, comment="项目封面")
    project_leader = Column(String(10), nullable=False, comment="项目负责人")
    project_description = Column(String(500), nullable=False, comment="项目描述")
    is_active = Column(Boolean, default=True, comment="是否删除")
    created_time = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated_time = Column(TIMESTAMP, nullable=False, default=datetime.now())
