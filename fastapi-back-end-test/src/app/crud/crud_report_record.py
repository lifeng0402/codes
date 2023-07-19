#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: crud_report_record.py
@时间: 2023/07/19 20:53:24
@说明: 
"""

from sqlalchemy import (
    select, update, delete, insert,
    and_
)
from sqlalchemy.orm import Session
from src.app.models.models_report import (
    Report, ReportRecord
)
from src.app.cabinet.transition import Transition
from src.app.excpetions.debug_test import DebugTestException


__all__ = [
    "ReportRecord"
]


class ReportRecord:
    def __init__(self, session: Session) -> None:
        self.r = Report
        self.db = session
        self.rd = ReportRecord

    def create_record(self, succeed_results: dict, defeated_results: dict, error_results: str, report_id: int):
        try:

            if not self.db.execute(
                select(self.r).where(self.r.id == report_id)
            ).scalars().first():
                raise DebugTestException(message="数据不存在或被删除...")

            results = self.rd(
                succeed_results=succeed_results,
                defeated_results=defeated_results,
                error_results=error_results, report_id=report_id,
            )
            self.db.add(results)
            self.db.commit()
            self.db.refresh(results)
        except Exception as exc:
            raise exc
