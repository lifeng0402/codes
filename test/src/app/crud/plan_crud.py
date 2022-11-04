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
            do_logger.error(f"计划添加失败: {str(ex)}")
            raise ex

    def plan_update(self, *, plan: plan_schemas.PlanUpdate):
        """
        更新测试计划
        :param plan:
        :return:
        """
        try:
            # 查询数据是否存在
            datas_info = self._session.execute(select(self._plan).where(self._plan.id == plan.plan_id))
            # 如果数据存在则抛出异常
            if not datas_info.scalars().first():
                raise Exception("测试计划不存在 ！")

            # 执行数据更新操作
            datas_info = self._session.execute(
                update(self._plan).values(name=plan.name, principal=plan.principal).where(self._plan.id == plan.plan_id)
            )
            # 提交并更新数据库
            self._session.add(datas_info)
            self._session.commit()
            self._session.refresh(datas_info)

            # 查询更新后的数据
            results_info = self._session.execute(
                select(
                    [self._plan.id, self._plan.name, self._plan.principal]
                ).where(self._plan.id == plan.plan_id)
            ).fetchone()

            return self._plan.is_json(results=results_info)


        except Exception as ex:
            do_logger.error(ex)
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
                    [self._plan.id, self._plan.name, self._plan.principal, self._plan.created_time]
                ).where(self._plan.is_active == 0).offset(skip).limit(limit)
            ).all()

            return self._plan.is_json(results=db_datas)

        except Exception as ex:
            do_logger.error(f"测试计划列表为空: {ex}")
            raise ex

    def plan_delete(self, *, plan_id: int):
        try:
            data_info = self._session.execute(select(self._plan).where(self._plan.id == plan_id)).fetchone()

            if not data_info:
                raise Exception("数据不存在 ！")

            # 执行删除数据的SQL方法
            self._session.execute(delete(self._plan).where(self._plan.id == plan_id))
            # 提交并更新数据库
            self._session.commit()
            data_info = self._session.execute(select(self._plan).where(self._plan.id == plan_id)).fetchone()

            if data_info:
                raise Exception("删除失败")

            return
        except Exception as ex:
            raise ex

    def plan_execute(self, *, case_id:plan_schemas.PlanData):
        pass
