#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: crud_report_record.py
@时间: 2023/07/19 20:53:24
@说明:
"""

import typing as ty
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
    "CrudReportRecord"
]


class CrudReportRecord:
    def __init__(self, session: Session) -> None:
        self.r = Report
        self.db = session
        self.rd = ReportRecord

    def create_record(self, response: ty.Union[dict, str, None], case_id: int, report_id: int):
        """
        新建测试报告记录数据

        :param response: 接口的返回值
        :type response: ty.Union[dict, str, None]
        :param case_id: 测试用例ID
        :type case_id: int
        :param report_id: 测试报告ID
        :type report_id: int
        :raises DebugTestException: 抛出异常
        :raises exc.message: 捕获异常错误
        :return: 
        :rtype: dict
        """
        try:
            if not self.db.execute(
                select(self.r).where(self.r.id == report_id)
            ).scalars().first():
                raise DebugTestException(message="数据不存在或被删除...")

            results = self.rd(
                response=response, case_id=case_id, report_id=report_id,
            )
            self.db.add(results)
            self.db.commit()
            self.db.refresh(results)
            return results.to_dict()
        except DebugTestException as exc:
            raise exc.message

    def insert_record(self, response: ty.Union[dict, str, None], case_id: int, report_id: int):
        """
        往测试记录表插入数据

        :param response: 返回值
        :type response: ty.Union[dict, str, None]
        :param case_id: 用例ID
        :type case_id: int
        :param report_id: 测试报告ID
        :type report_id: int
        :raises exc.message: 捕获异常错误
        """
        try:
            self.db.execute(
                insert(self.rd).values(
                    response=response, report_id=report_id, case_id=case_id
                )
            )
            self.db.commit()
            return
        except DebugTestException as exc:
            raise exc.message

    def report_record_detalis(self, report_id: int):
        """
        根据测试报告ID从测试报告记录表中获取数据

        :param report_id: 测试报告ID
        :type report_id: int
        :raises exc.message: 捕获异常错误
        :return: 
        :rtype: dict
        """
        try:
            results = self.db.execute(
                select(
                    self.rd.case_id,
                    self.rd.report_id,
                    self.rd.response,
                ).where(self.rd.report_id == report_id)
            ).fetchall()

            return dict(
                list=[Transition.proof_dict(i._asdict()) for i in results]
            )
        except DebugTestException as exc:
            raise exc.message
