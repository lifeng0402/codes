#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: cases_models.py
@时间: 2023/06/12 18:28:15
@说明:
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    JSON
)
from datetime import datetime
from src.app.public.db.base import Base

__all__ = [
    "Users"
]


class Cases(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    method = Column(String(10), nullable=True)
    url = Column(String(200), nullable=True)
    content = Column(String(500), nullable=True)
    data = Column(String(500), nullable=True)
    files = Column(String(100), nullable=True)
    json = Column(JSON, nullable=True)
    params = Column(JSON, nullable=True)
    headers = Column(JSON, nullable=True)
    cookies = Column(JSON, nullable=True)
    timeout = Column(Integer, nullable=True)
    auth = Column(JSON, nullable=True)
    follow_redirects = Column(JSON, nullable=True)
    extensions = Column(JSON, nullable=True)
    created_time = Column(DateTime, default=datetime.now())
    updated_time = Column(DateTime, onupdate=datetime.now,default=datetime.now())
