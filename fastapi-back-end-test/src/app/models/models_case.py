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
    DateTime,
    Float,
    JSON
)
from json import dumps
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin
from src.app.core.database.base import Base


__all__ = [
    "Case"
]


class Case(Base, SerializerMixin):
    __tablename__ = "case"

    id = Column(Integer, primary_key=True, index=True)
    method = Column(String(20), nullable=False)
    url = Column(String(500), nullable=False)
    json = Column(JSON, nullable=True)
    data = Column(JSON, nullable=True)
    content = Column(String(500), nullable=True)
    files = Column(JSON, nullable=True)
    params = Column(JSON, nullable=True)
    headers = Column(JSON, nullable=True)
    cookies = Column(JSON, nullable=True)
    timeout = Column(Float, nullable=True)
    extract = Column(JSON, nullable=True)
    validate = Column(JSON, nullable=True)
    plan_id = Column(Integer, nullable=True)
    is_delete = Column(Integer, default=0)
    created_time = Column(DateTime, default=datetime.now())
    updated_time = Column(DateTime, onupdate=datetime.now,
                          default=datetime.now())

    def __init__(
        self, method, url, json=None, data=None, content=None, files=None,
        params=None, headers=None, cookies=None, timeout=None, plan_id=None
    ):
        self.url = url
        self.method = method
        self.content = content
        self.plan_id = plan_id
        self.timeout = timeout
        self.json = json
        self.data = data
        self.files = files
        self.params = params
        self.headers = headers
        self.cookies = cookies

    def __repr__(self):
        return f"""
            <Cases(
                  id='{self.id}', method='{self.method}', url='{self.url}', 
                  json_data='{self.json}',form_data='{self.data}', content='{self.content}', 
                  files='{self.files}', params='{self.params}', headers='{self.headers}', 
                  cookies='{self.cookies}', timeout='{self.timeout}'
            )>
        """
