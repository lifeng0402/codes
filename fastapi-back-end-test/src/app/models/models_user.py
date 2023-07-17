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
    DateTime
)
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin
from src.app.core.db.base import Base


__all__ = [
    "User"
]


class User(Base, SerializerMixin):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=True)
    password = Column(String(500), nullable=True)
    is_delete = Column(Integer, default=0)
    created_time = Column(DateTime, default=datetime.now())
    updated_time = Column(DateTime, onupdate=datetime.now,
                          default=datetime.now())

    def __repr__(self):
        return f"""
            <Users(
                  id='{self.id}', username='{self.username}', password='{self.password}', is_delete='{self.is_delete}'
            )>
        """
