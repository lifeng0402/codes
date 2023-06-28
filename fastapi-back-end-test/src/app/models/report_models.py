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
    JSON
)
from json import (
    dumps, loads
)
from datetime import datetime
from src.app.core.db.base import Base
from src.app.excpetions.custom_json import (
    DateTimeEncoder, CustomJSONEncoder
)


__all__ = [
    "Users"
]


class Report(Base):
    __tablename__ = "report"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(10), nullable=False)
    total_num = Column(Integer, nullable=False)
    defeated_num = Column(Integer, nullable=False)
    succeed_num = Column(Integer, nullable=False)
    created_time = Column(DateTime, default=datetime.now())
    updated_time = Column(DateTime, onupdate=datetime.now,
                          default=datetime.now())

    def __init__(self, title, total_num, defeated_num, succeed_num):
        self.title = title
        self.total_num = total_num
        self.defeated_num = defeated_num
        self.succeed_num = succeed_num

    def __repr__(self):
        return f"""
            <Report(
                  id='{self.id}', title='{self.title}', total_num='{self.total_num}', 
                  defeated_num='{self.defeated_num}',succeed_num='{self.succeed_num}'
            )>
        """


class ReportRecord(Base):
    __tablename__ = "report_record"

    id = Column(Integer, primary_key=True, index=True)
    defeated = Column(String(10), nullable=True)
    succeed = Column(Integer, nullable=True)
    error = Column(Integer, nullable=True)
    report_id = Column(Integer, nullable=True)
    created_time = Column(DateTime, default=datetime.now())
    updated_time = Column(DateTime, onupdate=datetime.now,
                          default=datetime.now())

    def __init__(self, defeated_num=None, succeed_num=None, error=None, report_id=None):
        self.defeated_num = defeated_num
        self.succeed_num = succeed_num
        self.error = error
        self.report_id = report_id

    def __repr__(self):
        return f"""
            <ReportRecord(
                  id='{self.id}', defeated_num='{self.defeated_num}', succeed_num='{self.succeed_num}', 
                  error='{self.error}',report_id='{self.report_id}'
            )>
        """
