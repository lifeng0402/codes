#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/8 09:01
# @Author  : debugfeng
# @Site    : 
# @File    : report_crud.py
# @Software: PyCharm


from sqlalchemy.orm import Session
from src.app.models import reportModels
from sqlalchemy import insert

__all__ = ["DatabasesReport"]


class DatabasesReport:
    def __init__(self, *, db: Session):
        self._session = db
        self._report = reportModels.Reposts

    def insert_reports_info(self, **kwargs):
        results = self._session.execute(
            insert(self._report).values(**kwargs)
        )
        self._session.commit()
        self._session.refresh(results)
