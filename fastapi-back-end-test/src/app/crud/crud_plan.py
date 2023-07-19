#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: plan_crud.py
@时间: 2023/06/20 19:05:54
@说明: 
"""

from sqlalchemy import (
    select, update, delete
)
from sqlalchemy.orm import Session
from src.app.models.models_plan import Plan
from src.app.models.models_case import Case
from src.app.schemas.plan import (
    PlanSchemas, PlanExcute
)
from src.app.cabinet.transition import Transition
from src.app.excpetions.debug_test import DebugTestException


class PlanCrud:
    def __init__(self, session: Session) -> None:
        self.c = Case
        self.p = Plan
        self.db = session

    def create_plan(self, data: PlanSchemas):
        """
        测试计划添加
        @param  :
        @return  :
        """
        try:
            # 传递参数
            results = self.p(
                title=data.title,
                environment=data.environment,
                description=data.description
            )
            # 添加数据并提交, 最后刷新数据
            self.db.add(results)
            self.db.commit()
            self.db.refresh(results)
            return Transition.proof_dict(results.to_dict())
        except Exception as e:
            raise e

    def update_plan(self, plan_id, data: PlanSchemas):
        try:
            results = self.db.execute(
                select(self.p.id).where(self.p.id == plan_id)
            ).scalars().first()

            if not results:
                raise DebugTestException(message="plan_id不存在...")

            self.db.execute(
                update(self.p).where(self.p.id == plan_id).values(
                    title=data.title,
                    environment=data.environment,
                    description=data.description
                )
            )
            self.db.commit()
            return
        except Exception as exc:
            raise Exception(exc)

    def list_plan(self, *, skip, limit):
        """
        测试计划列表
        @param  :
        @return  :
        """
        try:
            stmt = select(self.p).offset(skip).limit(limit)
            results = self.db.execute(stmt).fetchall()

            return dict(
                 list=[Transition.proof_dict(i._asdict()) for i in results]
            )
        except Exception as e:
            raise e

    def delete_plan(self, plan_id):
        try:
            results = self.db.execute(
                select(self.p.id).where(self.p.id == plan_id)
            ).scalars().first()

            if not results:
                raise DebugTestException(message="数据不存在或被移除...")

            self.db.execute(delete(self.p).where(self.p.id == plan_id))
            self.db.commit()
            return
        except Exception as e:
            raise e

    def execute_plan(self, data: PlanExcute):
        try:
            if not self.db.execute(
                select(self.p).where(data.plan_id == self.p.id)
            ).scalars().first():
                raise DebugTestException(message="plan_id不存在...")

            results = self.db.execute(
                select(
                    self.c.id, self.c.method, self.c.url,
                    self.c.json, self.c.data, self.c.params, self.c.headers,
                    self.c.cookies, self.c.files, self.c.content, self.c.timeout
                ).where(data.plan_id == self.c.plan_id)
            ).fetchall()

            return dict(
                list=[i._asdict() for i in results]
            )
        except Exception as exc:
            raise exc
