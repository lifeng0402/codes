#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/29 15:04
# @Author  : debugfeng
# @Site    : 
# @File    : project_crud.py
# @Software: PyCharm

from sqlalchemy import select, and_, not_
from sqlalchemy.orm import Session
from src.app.models import datas_model
from src.app.public.logger import do_logger
from src.app.schemas.project import cases_schemas
from src.app.enumeration.request_enum import BodyType
from src.app.public.databases import database_commit


class DatabaseProject:
    def __init__(self, *, db: Session):
        self._session = db
        self._datas = datas_model.Datas

    def cases_data(self, *, case: cases_schemas.CaseDatas):
        try:
            datas_info = self._session.execute(
                select(
                    [
                        self._datas.id, self._datas.title, self._datas.method, self._datas.url,
                        self._datas.headers, self._datas.body_type, self._datas.body, self._datas.params,
                        self._datas.cookies, self._datas.actual, self._datas.expect
                    ]
                ).where(and_(self._datas.id.in_(case.case_id), self._datas.is_active == 1))
            ).all()
            return [dict(zip(datas.keys(), datas)) for datas in datas_info]
        except Exception as ex:
            do_logger.error(f"未查询到指定数据: {ex}")
            raise ex
