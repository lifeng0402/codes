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
    select, update, delete
)
from sqlalchemy.orm import Session
from src.app.models.plan_models import Plan
from src.app.models.cases_models import Cases
from src.app.core.db.session import session_commit
from src.app.schemas.cases_schemas import (
    RequestSchemas, DeleteCases
)


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
            results = session_commit(self.db, datas=case_info)

            return results
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
            if not isinstance(datas, dict):
                return datas if datas else None
            return json.dumps(datas, ensure_ascii=False)

        try:
            if self.db.execute(select(Cases)).scalars().first():
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
            if case_id is None:
                return None, "数据不存在或被移除..."

            # 执行删除操作
            self.db.execute(
                delete(Cases).where(Cases.id == case_id)
            )
            self.db.commit()

            return None, "删除成功..."

        except Exception as e:
            raise e

    def case_batch_delete(self, *, case_id: DeleteCases):
        """
        根据数组case_id查询到数据,再执行删除操作
        @param  :
        @return  :
        """
        print(case_id, 222)
        try:
            return case_id.case_id
            # case_list = Cases.id.in_(case_id.case_id)
            # # 判断数据是否存在
            # if not case_list:
            #     return None, "数据不存在或被移除..."

            # # 执行删除操作
            # self.db.execute(delete(Cases).where(case_list))
            # self.db.commit()

            # return None, "删除成功..."

        except Exception as e:
            raise e
