#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: cases_crud.py
@时间: 2023/06/16 13:56:06
@说明:
"""

from sqlalchemy import (
    select
)
from sqlalchemy.orm import Session
from src.app.models.cases_models import Cases
from src.app.models.plan_models import Plan
from src.app.core.db.session import session_commit
from src.app.schemas.cases_schemas import RequestSchemas


class CasesCrud:
    def __init__(self, session: Session) -> None:
        self.db = session

    def save_cases(self, data: RequestSchemas):

        def select_plan(*, db: Session, plan_id: int or str):
            # 查询计划ID是否存在,不存在就抛出异常
            results = db.execute(
                select(Plan).where(Plan.id == plan_id)
            )
            if results.scalars().first():
                return
            raise Exception("plan_id不存在...")

        try:
            case_info = Cases(
                method=data.method, url=data.url,
                body=self.transition(data.body),
                files=data.files, content=data.content,
                timeout=data.timeout, body_type=data.body_type,
                expected_result=self.transition(data.expected_result), plan_id=data.plan_id,
                cookies=self.transition(data.cookies), headers=self.transition(data.headers)
            )
            # 如果计划ID为真值
            if data.plan_id:
                return select_plan(db=self.db, plan_id=data.plan_id)
            # 往数据库提交数据
            results = session_commit(self.db, datas=case_info)
            return Cases.as_dict(results)
        except Exception as e:
            raise e

    def case_list(self, *, skip: int = 1, limit: int = 10):
        """
        测试用例列表查询
        @param  :
        @return  :
        """
        try:
            results = self.db.execute(
                select([Cases]).limit(limit).offset(skip)
            ).fetchall()
            return {"list": results}
        except Exception as e:
            raise e

    @staticmethod
    def transition(data):
        """
        把字典或者字符串类型转成字符串格式, 并把值返回
        @param  :
        @return  :
        """
        if data is not None:
            return data if isinstance(data, str) else str(data)
        return data
