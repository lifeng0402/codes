#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/18 18:18
# @Author  : debugfeng
# @Site    : 
# @File    : plan_crud.py
# @Software: PyCharm

from sqlalchemy.orm import Session
from src.app.models import plan_model
from src.app.public.logger import do_logger
from src.app.schemas.project import plan_schemas
from src.app.public.databases import database_commit
from sqlalchemy import select, and_, or_, update, delete

__all__ = ["DatabasesPlan"]


class DatabasesPlan:
    def __init__(self, *, db: Session):
        self._session = db
        self._plan = plan_model.Plan

    def plan_add(self, *, plan: plan_schemas.PlanAdd):
        """
        添加测试计划，新增到plan表中
        :param plan:
        :return:
        """

        try:
            # 查询数据是否存在
            datas_info = self._session.execute(select(self._plan).where(self._plan.name == plan.name))
            # 如果数据存在则抛出异常
            if datas_info.scalars().first():
                raise Exception(f"{plan.name} - 测试计划名称已存在 ！")

            db_datas = self._plan(name=plan.name, principal=plan.principal)
            # 提交数据成功后执行刷新
            database_commit(_session=self._session, _datas=db_datas)

            results_info = self._session.execute(
                select(
                    [self._plan.id, self._plan.name, self._plan.principal]
                ).where(self._plan.name == plan.name, self._plan.is_active == 0)
            ).fetchone()

            return results_info

        except Exception as ex:
            do_logger.error(f"测试计划添加失败: {str(ex)}")
            raise ex

    def plan_list(self, *, skip: int, limit: int):
        """
        获取测试计划列表数据
        :param skip:
        :param limit:
        :return:
        """
        try:
            db_datas = self._session.execute(
                select(
                    [
                        self._plan.id, self._plan.name, self._plan.principal, self._plan.created_time
                    ]
                ).where(self._plan.is_active == 0).offset(skip).limit(limit)
            ).all()

            return self._plan.is_json(results=db_datas)

        except Exception as ex:
            do_logger.error(f"测试计划列表为空: {ex}")
            raise ex
