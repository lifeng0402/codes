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
from src.app.models.models_plan import Plan
from src.app.core.db.session import session_commit
from src.app.schemas.plan import (
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
            return session_commit(self.db, datas=plan_info)
        except Exception as e:
            raise e

    def update_plan(self, plan_id, data: PlanSchemas):
        try:
            results = self.db.execute(
                select(Plan.id).where(Plan.id == plan_id)
            ).scalars().first()

            if not results:
                raise Exception("plan_id不存在...")

            self.db.execute(
                update(Plan).where(Plan.id == plan_id).values(
                    title=data.title,
                    environment=data.environment,
                    description=data.description
                )
            )
            self.db.commit()
            return
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

    def delete_plan(self, plan_id):
        try:
            results = self.db.execute(
                select(Plan.id).where(Plan.id == plan_id)
            ).scalars().first()

            if not results:
                raise Exception("数据不存在或被移除...")

            self.db.execute(
                delete(Plan).where(Plan.id == plan_id)
            )
            self.db.commit()
            return
        except Exception as e:
            raise e
