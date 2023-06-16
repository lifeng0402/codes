#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: cases_models.py
@时间: 2023/06/12 18:28:15
@说明:
"""

import json
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    JSON,
    Float,
    VARBINARY
)
from datetime import datetime
from src.app.core.db.base import Base

__all__ = [
    "Users"
]


class Cases(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    method = Column(String(10), nullable=False)
    url = Column(String(200), nullable=False)
    body_type = Column(String(10), nullable=False)
    body = Column(String(500), nullable=True)
    content = Column(String(500), nullable=True)
    files = Column(String(500), nullable=True)
    params = Column(String(500), nullable=True)
    headers = Column(String(500), nullable=True)
    cookies = Column(String(500), nullable=True)
    timeout = Column(Float, nullable=True)
    auth = Column(String(500), nullable=True)
    follow_redirects = Column(String(500), nullable=True)
    extensions = Column(String(500), nullable=True)
    expected_result = Column(String(500), nullable=True)
    created_time = Column(DateTime, default=datetime.now())
    updated_time = Column(DateTime, onupdate=datetime.now,
                          default=datetime.now())

    @staticmethod
    def handle_data(results):
        data = {
            k: v for k, v in results.__dict__.items() if v is not None
        }
        if '"\"' not in str(data):
            return data
        data = str(data).replace('"\"', "")
        return json.loads(data)
