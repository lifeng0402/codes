#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: cases_crud.py
@时间: 2023/06/16 13:56:06
@说明:
"""


import json
from sqlalchemy import (
    select, update, delete, and_
)
from sqlalchemy.orm import Session
from src.app.models.models_plan import Plan
from src.app.models.models_case import Case
from src.app.cabinet.transition import Transition
from src.app.schemas.case import (
    RequestSchemas, DeleteCases
)
from src.app.core.excpetions import DebugTestException


class CasesCrud:
    def __init__(self, session: Session) -> None:
        self.p = Plan
        self.c = Case
        self.db = session

    def create_cases(self, datas: RequestSchemas):
        """
        创建测试用例并存储到数据库中

        :param datas: 请求参数
        :type datas: RequestSchemas
        :raises DebugTestException: 抛出异常
        :raises DebugTestException: 抛出异常
        :raises exc.message: 捕获异常错误
        :return: 
        :rtype: dict
        """
        try:

            if datas.form_data and datas.json_data:
                raise DebugTestException(
                    message="form_data 和 json_data 字段不能同时存在.."
                )

            # 映射对应数据
            case_info = self.c(
                method=datas.method, url=datas.url, json=datas.json_data,
                data=datas.form_data, files=datas.files, content=datas.content,
                timeout=datas.timeout, plan_id=datas.plan_id, cookies=datas.cookies, headers=datas.headers
            )
            # 如果计划ID为真值
            if datas.plan_id:
                # 查询计划ID是否存在
                results = self.db.execute(
                    select(self.p).where(self.p.id == datas.plan_id)
                )
                # 判断数据是否存在
                if not results.scalars().first():
                    raise DebugTestException(message="plan_id不存在...")
                return

            # 往数据库提交数据
            self.db.add(case_info)
            self.db.commit()
            self.db.refresh(case_info)

            return Transition.proof_dict(case_info.to_dict())

        except DebugTestException as exc:
            raise exc.message

    def update_cases(self, case_id: int, data: RequestSchemas):
        """
        根据测试用例ID查询数据是否存在,不存在就抛出异常
        如果存在就根据测试用例ID执行数据更新操作

        :param case_id: 用例ID
        :type case_id: int
        :param data: 请求参数
        :type data: RequestSchemas
        :raises DebugTestException: 抛出异常
        :raises exc.message: 捕获异常错误
        """
        try:
            results = self.db.execute(
                select(self.c.id).where(self.c.id == case_id)
            ).scalars().first()

            if not results:
                raise DebugTestException(message="case_id不存在...")

            # 执行更新语句
            self.db.execute(
                update(self.c).where(self.c.id == case_id).values(
                    method=data.method, url=data.url,
                    json_data=data.json_data,
                    form_data=data.form_data,
                    files=data.files, content=data.content,
                    timeout=data.timeout, plan_id=data.plan_id,
                    cookies=data.cookies, headers=data.headers
                )
            )

            # 往数据库提交数据
            self.db.commit()

            return
        except DebugTestException as exc:
            raise exc.message

    def case_list(self, *, skip: int, limit: int):
        """
        查询测试用例表中的数据进行分页展示

        :param skip: 页码
        :type skip: int
        :param limit: 条数
        :type limit: int
        :raises exc: 捕获异常错误
        :return: 
        :rtype: dict
        """
        try:
            # 分页查询Cases表中的数据
            results = self.db.execute(select(self.c).offset(
                skip).limit(limit)).fetchall()

            return dict(
                list=[Transition.proof_dict(i._asdict()) for i in results]
            )
        except DebugTestException as exc:
            raise exc

    def case_delete(self, *, case_id: int):
        """
        根据测试用例ID从数据库删除指定数据

        :param case_id: 用例ID
        :type case_id: int
        :raises exc.message: 捕获异常错误
        :return: 
        :rtype: None
        """
        try:
            # 查询数据是否存在
            case_id = self.db.execute(
                select(self.c.id).where(self.c.id == case_id)
            ).scalars().first()

            # 不存在就抛异常提示
            if not case_id:
                return DebugTestException(message="数据不存在或被移除...")

            # 执行删除操作
            self.db.execute(delete(self.c).where(self.c.id == case_id))
            self.db.commit()

            return

        except DebugTestException as exc:
            raise exc.message

    def case_batch_delete(self, case: DeleteCases):
        """
        根据测试用例ID,从数据库批量删除测试用例

        :param case: 请求参数
        :type case: DeleteCases
        :raises DebugTestException: 抛出异常
        :raises exc.message: 捕获异常错误
        """
        try:
            # 根据case_id查询全部数据
            case_list = self.db.execute(
                select(self.c.id).where(self.c.id.in_(case.case_id))
            ).scalars().all()

            # 判断数据是否存在
            if not case_list:
                raise DebugTestException(message="数据不存在或被移除...")

            # 执行删除操作
            self.db.execute(delete(self.c).where(self.c.id.in_(case.case_id)))
            self.db.commit()

            return

        except DebugTestException as exc:
            raise exc.message
