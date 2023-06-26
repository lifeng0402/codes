#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: plan_crud.py
@时间: 2023/06/20 19:05:54
@说明: 
"""

import json
from sqlalchemy import (
    select, update, delete
)
from sqlalchemy.orm import Session
from src.app.models.plan_models import Plan
from src.app.schemas.plan_schemas import (
    PlanSchemas
)
from src.app.excpetions.custom_json import CustomJSONEncoder


class PlanCrud:
    def __init__(self, session: Session) -> None:
        self.db = session

    def create_plan(self, data: PlanSchemas):
        """
        测试计划添加
        @param  :
        @return  :
        """
        try:
            # 传递参数
            plan_info = Plan(
                title=data.title,
                environment=data.environment,
                description=data.description
            )
            # 添加数据并提交, 最后刷新数据
            self.db.add(plan_info)
            self.db.commit()
            self.db.refresh(plan_info)

            return plan_info
        except Exception as e:
            raise e

    def list_plan(self, *, skip, limit):
        """
        测试计划列表
        @param  :
        @return  :
        """
        try:
            plan_list = self.db.execute(
                select(Plan).offset(skip).limit(limit)
            ).scalars().all()

            return {"list": plan_list}
        except Exception as e:
            raise e
