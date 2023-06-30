#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: crud_repore.py
@时间: 2023/06/30 17:09:01
@说明:
"""

import json
import typing
from sqlalchemy import (
    select, update, delete, and_
)
from sqlalchemy.orm import Session
from src.app.models.models_report import (
    Report as r, ReportRecord as rr
)
from src.app.core.db.session import session_commit
from src.app.schemas.case import (
    RequestSchemas, DeleteCases, BatchTestCaseRequest
)
from src.app.excpetions.custom_json import CustomJSONEncoder


class ReportCrud:
    def __init__(self, session: Session) -> None:
        self.db = session

    def create_number(self, *, title: str, total: int = 0, total_succeed: int = 0, total_defeated: int = 0):
        try:
            data_info = self.db.execute(
                r(
                    title=title, total=total,
                    total_succeed=total_succeed, total_defeated=total_defeated
                )
            )
            self.db.add(data_info)
            self.db.commit()
            self.db.refresh(data_info)
            return
        except Exception as e:
            raise e

    def update_number(self, *, report_id: int, total: int, total_succeed: int, total_defeated: int):
        try:
            update(r).where(r.id == report_id).values(
                total=r.total + total,
                total_succeed=r.total_succeed + total_succeed,
                total_defeated=r.total_defeated + total_defeated
            )

            self.db.commit()
            return
        except Exception as e:
            raise e
