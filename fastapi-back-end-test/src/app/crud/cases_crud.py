#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: cases_crud.py
@时间: 2023/06/16 13:56:06
@说明:
"""


import datetime
from sqlalchemy.orm import Session
from src.app.models.cases_models import Cases
from src.app.schemas.cases_schemas import RequestSchemas


class CasesCrud:
    def __init__(self, session: Session) -> None:
        self.db = session

    def save_cases(self, data: RequestSchemas):
        try:
            case_info = Cases(
                method=data.method, url=data.url,
                body=self.transition(data.body),
                auth=self.transition(data.auth),
                files=data.files, content=data.content,
                timeout=data.timeout, body_type=data.body_type,
                extensions=data.extensions,
                follow_redirects=data.follow_redirects,
                expected_result=self.transition(data.expected_result),
                cookies=self.transition(data.cookies), headers=self.transition(data.headers)
            )
            # 往数据库添加数据
            self.db.add(case_info)
            # 往数据库提交数据
            self.db.commit()
            # 刷新提交的数据
            self.db.refresh(case_info)
            return Cases.as_dict(case_info)
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
