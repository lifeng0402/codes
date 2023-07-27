#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: plan_models.py
@时间: 2023/06/20 08:15:59
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
from src.app.core.database.base import Base


class Plan(Base, SerializerMixin):
    __tablename__ = "plan"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    environment = Column(Integer, nullable=False)
    description = Column(String(500), nullable=True)
    is_delete = Column(Integer, default=0)
    created_time = Column(DateTime, default=datetime.now())
    updated_time = Column(DateTime, onupdate=datetime.now,
                          default=datetime.now())

    def __init__(self, title, environment=None, description=None):
        self.title = title
        self.environment = environment
        self.description = description

    def __repr__(self):
        return f"""
            <Plan(
                  id='{self.id}', name='{self.title}', environment='{self.environment}', description='{self.description}'
            )>
        """
