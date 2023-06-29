#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: cases_crud.py
@时间: 2023/06/16 13:56:06
@说明:
"""


import json
import typing
from sqlalchemy import (
    select, update, delete, and_
)
from sqlalchemy.orm import Session
from src.app.models.models_plan import Plan
from src.app.models.models_case import Cases
from src.app.core.db.session import session_commit
from src.app.schemas.case import (
    RequestSchemas, DeleteCases, BatchTestCaseRequest
)
from src.app.excpetions.custom_json import CustomJSONEncoder


class CasesCrud:
    def __init__(self, session: Session) -> None:
        self.db = session

    def save_cases(self, data: RequestSchemas):
        """
        对data中的数据进行存储到数据库
        @param  :
        @return  :
        """

        def select_plan(*, db: Session, plan_id: int or str):
            # 查询计划ID是否存在,不存在就抛出异常
            results = db.execute(
                select(Plan).where(Plan.id == plan_id)
            )
            # 判断数据是否存在
            if results.scalars().first():
                return
            raise Exception("plan_id不存在...")

        try:
            # 映射对应数据
            case_info = Cases(
                method=data.method, url=data.url, body=data.body, files=data.files,
                content=data.content, timeout=data.timeout, body_type=data.body_type,
                expected_result=data.expected_result, plan_id=data.plan_id,
                cookies=data.cookies, headers=data.headers
            )
            # 如果计划ID为真值
            if data.plan_id:
                return select_plan(db=self.db, plan_id=data.plan_id)

            # 往数据库提交数据
            return session_commit(self.db, datas=case_info)
        except Exception as e:
            raise e

    def update_cases(self, case_id: int, data: RequestSchemas):
        """
        根据case_id进行查询数据是否存在
        如存在则执行更新测试用例
        否则就抛出异常错误
        @param  :
        @return  :
        """

        def transition(datas: dict):
            """
            如果是字典则转成json
            否则就返回原值
            @param  :
            @return  :
            """
            return json.dumps(datas, ensure_ascii=False, cls=CustomJSONEncoder) if datas else datas

        try:
            results = self.db.execute(
                select(Cases.id).where(Cases.id == case_id)
            ).scalars().first()

            if not results:
                raise Exception("case_id不存在...")

            # 执行更新语句
            self.db.execute(
                update(Cases).where(Cases.id == case_id).values(
                    method=data.method, url=data.url,
                    body=transition(data.body),
                    files=transition(data.files),
                    content=data.content, timeout=data.timeout,
                    body_type=data.body_type, plan_id=data.plan_id,
                    expected_result=transition(data.expected_result),
                    cookies=transition(data.cookies), headers=transition(data.headers)
                )
            )

            # 往数据库提交数据
            self.db.commit()

            return
        except Exception as e:
            raise e

    def case_list(self, *, skip: int, limit: int):
        """
        测试用例列表查询
        @param  :
        @return  :
        """
        try:
            # 分页查询Cases表中的数据
            results = self.db.execute(
                select(Cases).offset(skip).limit(limit)
            ).scalars().all()

            return {"list": results}
        except Exception as e:
            raise e

    def case_delete(self, *, case_id: int):
        """
        根据case_id查询到数据,再执行删除操作
        @param  :
        @return  :
        """
        try:
            # 查询数据是否存在
            case_id = self.db.execute(
                select(Cases.id).where(Cases.id == case_id)
            ).scalars().first()

            # 不存在就抛异常提示
            if not case_id:
                return Exception("数据不存在或被移除...")

            # 执行删除操作
            self.db.execute(
                delete(Cases).where(Cases.id == case_id)
            )
            self.db.commit()

            return

        except Exception as e:
            raise e

    def case_batch_delete(self, case: DeleteCases):
        """
        根据数组case_id查询到数据,再执行删除操作
        @param  :
        @return  :
        """

        try:
            # 根据case_id查询全部数据
            case_list = self.db.execute(
                select(Cases.id).where(Cases.id.in_(case.case_id))
            ).scalars().all()

            # 判断数据是否存在
            if not case_list:
                raise Exception("数据不存在或被移除...")

            # 执行删除操作
            self.db.execute(delete(Cases).where(Cases.id.in_(case.case_id)))
            self.db.commit()

            return

        except Exception as e:
            raise e

    def cases_running(self, case_ids: BatchTestCaseRequest):
        """
        根据数组case_id查询到数据,再执行删除操作
        @param  :
        @return  :
        """
        def select_cases(condition: typing.Any):
            stmt = select(
                Cases.method, Cases.url, Cases.body_type, Cases.body, Cases.params,
                Cases.headers, Cases.cookies, Cases.content, Cases.files, Cases.expected_result
            ).where(condition)

            return stmt

        try:
            # 判断计划ID是否为真
            if case_ids.plan_id:
                case_list = self.db.execute(
                    select_cases(
                        condition=and_(
                            Cases.id.in_(case_ids.case_ids),
                            Cases.plan_id == case_ids.plan_id
                        )
                    )
                ).all()
            else:
                # 根据case_id查询全部数据
                case_list = self.db.execute(
                    select_cases(condition=Cases.id.in_(case_ids.case_ids))
                ).all()

            # 判断数据是否存在
            if not case_list:
                raise Exception("数据不存在或被移除...")

            return [row._asdict() for row in case_list]

        except Exception as e:
            raise e