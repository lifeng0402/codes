#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: models_response.py
@时间: 2023/07/19 08:23:34
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
from json import dumps
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin
from src.app.core.database.base import Base
from src.app.core.excpetions import CustomJSONEncoder


__all__ = [
    "Expected"
]


class Expected(Base, SerializerMixin):
    __tablename__ = "expected"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String(20))
    expected_result = Column(JSON, nullable=True)
    case_id = Column(Integer, nullable=True)
    is_delete = Column(Integer, default=0)
    created_time = Column(DateTime, default=datetime.now())
    updated_time = Column(DateTime, onupdate=datetime.now,
                          default=datetime.now())

    def __init__(
        self, symbol=None, expected_result=None, case_id=None
    ):
        self.symbol = symbol,
        self.case_id = case_id
        self.expected_result = expected_result

    def __repr__(self):
        return f"""
            <Cases(
                  symbol='{self.symbol}', case_id='{self.case_id}', expected_result='{self.expected_result}'
            )>
        """
