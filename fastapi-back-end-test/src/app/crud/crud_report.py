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

    def create_report(self, total: int = 0, total_succeed: int = 0, total_defeated: int = 0, total_error: int = 0):
        """
        创建测试报告存入数据库

        :param total: 用例总数, defaults to 0
        :type total: int
        :param total_succeed: 成功总数, defaults to 0
        :type total_succeed: int
        :param total_defeated: 失败总数, defaults to 0
        :type total_defeated: int
        :param total_error: 错误总数, defaults to 0
        :type total_error: int
        :raises exc.message: 捕获异常错误
        :return: 
        :rtype: dict
        """
        try:
            title: str = "测试报告"

            # 计算成功率,四舍五入保留2位小数
            # success_rate = round((total_succeed / total) * 100, 2)

            results = self.r(
                title=title, total=total,
                total_succeed=total_succeed,
                total_defeated=total_defeated,
                total_error=total_error, success_rate=float(0)
            )
            self.db.add(results)
            self.db.commit()
            self.db.refresh(results)
            results = Transition.proof_dict(results.to_dict())
            return dict(report_id=results["id"])
        except DebugTestException as exc:
            raise exc.message

    def update_report(self, *, report_id: int, total: int, total_succeed: int, total_defeated: int, total_error: int):
        """
        根据测试报告ID往数据库指定数据更新数据

        :param report_id: 测试报告ID
        :type report_id: int
        :param total: 用例总数
        :type total: int
        :param total_succeed: 成功总数
        :type total_succeed: int
        :param total_defeated: 失败总数
        :type total_defeated: int
        :param total_error: 错误总数
        :type total_error: int
        :raises exc.message: 捕获异常错误
        :return: 
        :rtype: dict
        """
        try:
            # 计算成功率,四舍五入保留2位小数
            success_rate = round((total_succeed / total) * 100, 2)

            # 执行更新操作
            self.db.execute(
                update(self.r).where(self.r.id == report_id).values(
                    total=total, total_succeed=total_succeed,
                    total_defeated=total_defeated, total_error=total_error, success_rate=success_rate
                )
            )

            self.db.commit()
            return dict(report_id=report_id)
        except DebugTestException as exc:
            raise exc.message

    def report_details(self, report_id: int):
        """
        根据测试报告ID查询数据

        :param report_id: 测试报告ID
        :type report_id: int
        :raises DebugTestException: 抛出异常
        :raises exc.message: 捕获异常错误
        :return: 
        :rtype: dict
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
        except DebugTestException as exc:
            raise exc.message
