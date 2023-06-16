#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: cases_crud.py
@时间: 2023/06/16 13:56:06
@说明:
"""


import json
from ast import literal_eval
from sqlalchemy.orm import Session
from src.app.models.cases_models import Cases
from src.app.schemas.cases_schemas import RequestSchemas


class CasesCrud:
    def __init__(self, session: Session) -> None:
        self.db = session

    def save_cases(self, data: RequestSchemas):
        try:
            case_info = Cases(
                method=data.method,
                url=data.url,
                auth=data.auth,
                files=data.files,
                content=data.content,
                timeout=data.timeout,
                body_type=data.body_type,
                extensions=data.extensions,
                body=self.transition_json(data.body),
                expected_result=data.expected_result,
                follow_redirects=data.follow_redirects,
                cookies=self.transition_json(data.cookies),
                headers=self.transition_json(data.headers)
            )
            # 往数据库添加数据
            self.db.add(case_info)
            # 往数据库提交数据
            self.db.commit()
            # 刷新提交的数据
            self.db.refresh(case_info)
            res = {k: v for k, v in case_info.__dict__.items() if v is not None}
            return Cases.handle_data(case_info)
        except Exception as e:
            raise e

    @staticmethod
    def transition_json(data: dict or str):
        """
        把字典或者字符串类型转成json格式, 并把值返回
        @param  :
        @return  :
        """
        if not isinstance(data, dict) or isinstance(data, str):
            return data
        return json.dumps(data)