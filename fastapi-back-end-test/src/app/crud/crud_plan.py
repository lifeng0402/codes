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
from src.app.models.models_plan import Plan as p
from src.app.core.db.session import session_commit
from src.app.schemas.plan import (
    PlanSchemas
)
from src.app.cabinet.transition import Transition
from src.app.excpetions.debug_test import CustomJSONEncoder


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
            plan_results = p(
                title=data.title,
                environment=data.environment,
                description=data.description
            )
            # 添加数据并提交, 最后刷新数据
            self.db.add(plan_results)
            self.db.commit()
            self.db.refresh(plan_results)
            return Transition.proof_dict(plan_results)
        except Exception as e:
            raise e

    def update_plan(self, plan_id, data: PlanSchemas):
        try:
            results = self.db.execute(
                select(p.id).where(p.id == plan_id)
            ).scalars().first()

            if not results:
                raise Exception("plan_id不存在...")

            self.db.execute(
                update(p).where(p.id == plan_id).values(
                    title=data.title,
                    environment=data.environment,
                    description=data.description
                )
            )
            self.db.commit()
            return
        except Exception as exc:
            raise Exception(f"错误信息：{exc}")

    def list_plan(self, *, skip, limit):
        """
        测试计划列表
        @param  :
        @return  :
        """
        try:
            stmt = select(p).offset(skip).limit(limit)
            plan_results = self.db.execute(stmt).scalars().all()

            return dict(
                list=Transition.proof_dict(plan_results.to_dict())
            )
        except Exception as e:
            raise e

    def delete_plan(self, plan_id):
        try:
            results = self.db.execute(
                select(p.id).where(p.id == plan_id)
            ).scalars().first()

            if not results:
                raise Exception("数据不存在或被移除...")

            self.db.execute(delete(p).where(p.id == plan_id))
            self.db.commit()
            return
        except Exception as e:
            raise e
