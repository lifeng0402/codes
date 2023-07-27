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
from src.app.core.excpetions import DebugTestException


class PlanCrud:
    def __init__(self, session: Session) -> None:
        self.c = Case
        self.p = Plan
        self.db = session

    def create_plan(self, data: PlanSchemas):
        """
        新建测试计划, 往数据库添加数据

        :param data: 请求参数
        :type data: PlanSchemas
        :raises exc.message: 捕获异常错误
        :return: 
        :rtype: json
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
        except DebugTestException as exc:
            raise exc.message

    def update_plan(self, plan_id: int, data: PlanSchemas):
        """
        先根据计划ID先执行查询验证计划ID是否存在
        最后执行update更新数据操作

        :param plan_id: 计划ID
        :type plan_id: int
        :param data: 请求参数
        :type data: PlanSchemas
        :raises DebugTestException: 抛出异常错误
        :raises exc.message: 捕获异常错误
        """
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
        except DebugTestException as exc:
            raise exc.message

    def list_plan(self, *, skip: int, limit: int):
        """
        直接查询全部测试计划并进行分页操作

        :param skip: 页码
        :type skip: int
        :param limit: 条数
        :type limit: int
        :raises exc.message: 捕获异常错误
        :return: 
        :rtype: json
        """
        try:
            stmt = select(self.p).offset(skip).limit(limit)
            results = self.db.execute(stmt).fetchall()

            return dict(
                list=[Transition.proof_dict(i._asdict()) for i in results]
            )
        except DebugTestException as exc:
            raise exc.message

    def delete_plan(self, plan_id: int):
        """
        根据计划ID把数据从数据库删除

        :param plan_id: 计划ID
        :type plan_id: int
        :raises DebugTestException: 抛出异常
        :raises exc.message: 捕获异常错误
        """
        try:
            results = self.db.execute(
                select(self.p.id).where(self.p.id == plan_id)
            ).scalars().first()

            if not results:
                raise DebugTestException(message="数据不存在或被移除...")

            self.db.execute(delete(self.p).where(self.p.id == plan_id))
            self.db.commit()
            return
        except DebugTestException as exc:
            raise exc.message

    def execute_plan(self, data: PlanExcute):
        """
        查询与计划关联的测试用例并返回

        :param data: 请求参数
        :type data: PlanExcute
        :raises DebugTestException: 抛出异常
        :raises exc.message: 捕获异常错误
        :return: 
        :rtype: dict
        """
        try:
            if not self.db.execute(
                select(self.p).where(data.plan_id == self.p.id)
            ).scalars().first():
                raise DebugTestException(message="plan_id不存在...")

            results = self.db.execute(
                select(
                    self.c.id, self.c.method, self.c.url,
                    self.c.json, self.c.data, self.c.params, self.c.headers, self.c.cookies,
                    self.c.files, self.c.content, self.c.timeout, self.c.extract, self.c.checkout
                ).where(data.plan_id == self.c.plan_id)
            ).fetchall()

            return dict(list=[i._asdict() for i in results])
        except DebugTestException as exc:
            raise exc.message
