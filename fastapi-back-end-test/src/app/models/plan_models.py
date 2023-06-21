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
from json import (
    dumps, loads
)
from sqlalchemy.orm import (
    relationship,
    backref
)
from datetime import datetime
from src.app.core.db.base import Base
from src.app.models.cases_models import Cases


class Plan(Base):
    __tablename__ = "plan"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    environment = Column(Integer, nullable=False)
    description = Column(String(500), nullable=True)
    created_time = Column(DateTime, default=datetime.now())
    updated_time = Column(DateTime, onupdate=datetime.now,
                          default=datetime.now())
    
    plan = relationship("Cases", backref="plan", lazy="dynamic")

    def __repr__(self):
        return f"""
            <Plan(
                  id='{self.id}', 
                  name='{self.title}', 
                  environment='{self.environment}', 
                  description='{self.description}'
            )>
        """
