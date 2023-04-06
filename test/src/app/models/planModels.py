#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/18 18:10
# @Author  : debugfeng
# @Site    :
# @File    : plan_model.py
# @Software: PyCharm

from typing import Any
from src.app.models import *

__all__ = ["Plan"]

Base = declarative_base()


class Plan(Base):
    __tablename__ = "plan"

    # 测试计划表
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False, comment="计划名称")
    domain_name = Column(String(50), nullable=False, comment="域名")
    environment = Column(String(50), nullable=False, comment="运行环境")
    is_active = Column(Boolean, default=False, comment="是否被删除")
    created_time = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated_time = Column(TIMESTAMP, nullable=False, default=datetime.now())

    @staticmethod
    def is_json(*, results: Any):
        data_list = []
        for data in results:
            results = dict(zip(data.keys(), data))
            # results["datas"] = json.loads(results["datas"])
            data_list.append(results)
        return data_list
