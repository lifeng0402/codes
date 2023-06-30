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
    DateTime
)
from datetime import datetime
from src.app.core.db.base import Base


__all__ = [
    "User"
]


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    mobile = Column(String(20), nullable=True)
    username = Column(String(20), nullable=True)
    password = Column(String(50), nullable=True)
    mailbox = Column(String(100), nullable=True)
    is_delete = Column(Boolean, default=False)
    created_time = Column(DateTime, default=datetime.now())
    updated_time = Column(DateTime, onupdate=datetime.now,
                          default=datetime.now())

    def __repr__(self):
        return f"""
            <Users(
                  id='{self.id}', mobile='{self.mobile}', username='{self.username}', 
                  password='{self.password}', mailbox='{self.mailbox}', is_delete='{self.is_delete}'
            )>
        """
