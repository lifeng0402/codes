#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: crud_repore.py
@时间: 2023/06/30 17:09:01
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
    "ReportCrud"
]


class ReportCrud:
    def __init__(self, session: Session) -> None:
        self.r = Report
        self.db = session
        self.rd = ReportRecord

    def create_report(self, total: int, total_succeed: int, total_defeated: int, total_error: int, success_rate: float):
        """
        创建测试报告概括数据
        @param  :
        @return  :
        """
        try:
            title: str = "测试报告"

            results = self.r(
                title=title, total=total, total_succeed=total_succeed,
                total_defeated=total_defeated, total_error=total_error, success_rate=success_rate
            )
            self.db.add(results)
            self.db.commit()
            self.db.refresh(results)
            results = Transition.proof_dict(results.to_dict())
            return dict(report_id=results["id"])
        except Exception as e:
            raise DebugTestException(message=e)

    def update_number(self, *, report_id: int, total: int, total_succeed: int, total_defeated: int, total_error: int):
        try:
            update(self.r).where(self.r.id == report_id).values(
                total=total, total_succeed=total_succeed,
                total_defeated=total_defeated, total_error=total_error
            )

            self.db.commit()
            return
        except Exception as e:
            raise e

    def report_details(self, report_id: int):
        """
        根据报告ID,查询测试报告概括详情
        @param  :
        @return  :
        """
        try:
            results = self.db.execute(
                select(
                    self.r.id, self.r.title,
                    self.r.total, self.r.total_succeed,
                    self.r.total_defeated, self.r.total_error, self.r.success_rate
                ).where(self.r.id == report_id)
            ).first()

            if not results:
                raise DebugTestException(message="数据不存在或被删除...")

            return Transition.proof_dict(results._asdict())
        except Exception as e:
            raise DebugTestException(message=e)
