#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: users.py
@时间: 2023/05/31 19:59:23
@说明: 
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    TIMESTAMP
)
from datetime import datetime
from src.app.public.db.base import Base


__all__ = [
    "Users"
]


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    mobile = Column(String(20), nullable=True)
    username = Column(String(20), nullable=True)
    password = Column(String(50), nullable=True)
    mailbox = Column(String(100), nullable=True)
    is_delete = Column(Boolean, default=False)
    created_time = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated_time = Column(TIMESTAMP, nullable=False, default=datetime.now())