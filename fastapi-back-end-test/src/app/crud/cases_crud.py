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
from src.app.core.db.session import session_commit
from src.app.schemas.cases_schemas import RequestSchemas


class CasesCrud:
    def __init__(self, session: Session) -> None:
        self.db = session

    def save_cases(self, data: RequestSchemas):
        try:
            case_info = Cases(
                method=data.method, url=data.url,
                body=self.transition(data.body),
                files=data.files, content=data.content,
                timeout=data.timeout, body_type=data.body_type,
                expected_result=self.transition(data.expected_result), plan_id=data.plan_id,
                cookies=self.transition(data.cookies), headers=self.transition(data.headers)
            )
            if not data.plan_id:
                pass
            # 往数据库提交数据
            results = session_commit(self.db, datas=case_info)
            return Cases.as_dict(results)
        except Exception as e:
            raise e

    def case_list(self, *, skip: int, limit: int):
        """
        测试用例列表查询
        @param  :
        @return  :
        """
        try:
            results = self.db.query(Cases).offset(skip).limit(limit).all()
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
