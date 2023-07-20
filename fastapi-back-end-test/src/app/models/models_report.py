#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: report_models.py
@时间: 2023/06/28 17:13:32
@说明: 
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Float,
    JSON,
    Text
)
from datetime import datetime
from src.app.core.db.base import Base
from sqlalchemy_serializer import SerializerMixin


__all__ = [
    "Report", "ReportRecord"
]


class Report(Base, SerializerMixin):
    __tablename__ = "report"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    total = Column(Integer, default=0)
    total_succeed = Column(Integer, default=0)
    total_defeated = Column(Integer, default=0)
    total_error = Column(Integer, default=0)
    success_rate = Column(Float, default=0)
    is_delete = Column(Integer, default=0)
    created_time = Column(DateTime, default=datetime.now())
    updated_time = Column(DateTime, onupdate=datetime.now,
                          default=datetime.now())

    def __init__(self, title, total, total_succeed, total_defeated, total_error, success_rate):
        self.title = title
        self.total = total
        self.total_succeed = total_succeed
        self.total_defeated = total_defeated
        self.total_error = total_error
        self.success_rate = success_rate

    def __repr__(self):
        return f"""
            <Report(
                  id='{self.id}', title='{self.title}', total='{self.total}', total_succeed='{self.total_succeed}',
                  total_defeated='{self.total_defeated}',total_error='{self.total_error}',success_rate='{self.success_rate}'
            )>
        """


class ReportRecord(Base, SerializerMixin):
    __tablename__ = "report_record"

    id = Column(Integer, primary_key=True, index=True)
    response = Column(JSON, nullable=True)
    case_id = Column(Integer, nullable=True)
    report_id = Column(Integer, nullable=True)
    created_time = Column(DateTime, default=datetime.now())
    updated_time = Column(DateTime, onupdate=datetime.now,
                          default=datetime.now())

    def __init__(self, response=None, case_id=None, report_id=None):
        self.response = response
        self.case_id = case_id
        self.report_id = report_id

    def __repr__(self):
        return f"""
            <ReportRecord(
                  id='{self.id}', response='{self.response}', report_id='{self.report_id}',case_id='{self.case_id}'
            )>
        """
