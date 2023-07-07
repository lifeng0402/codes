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
from json import (
    dumps, loads
)
from datetime import datetime
from src.app.core.db.base import Base
from src.app.excpetions.custom_json import (
    DateTimeEncoder, CustomJSONEncoder
)


__all__ = [
    "Case"
]


class Case(Base):
    __tablename__ = "case"

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
    expected_result = Column(String(500), nullable=True)
    plan_id = Column(Integer, nullable=True)
    is_delete = Column(Integer, default=0)
    created_time = Column(DateTime, default=datetime.now())
    updated_time = Column(DateTime, onupdate=datetime.now,
                          default=datetime.now())

    def __init__(
        self, method, url, body_type, body=None, content=None, files=None,
        params=None, headers=None, cookies=None, timeout=None, expected_result=None, plan_id=None
    ):
        self.url = url
        self.method = method
        self.content = content
        self.plan_id = plan_id
        self.timeout = timeout
        self.body_type = body_type
        self.body = self.dumps_data(body)
        self.files = self.dumps_data(files)
        self.params = self.dumps_data(params)
        self.headers = self.dumps_data(headers)
        self.cookies = self.dumps_data(cookies)
        self.expected_result = self.dumps_data(expected_result)

    def __repr__(self):
        return f"""
            <Cases(
                  id='{self.id}', method='{self.method}', url='{self.url}', 
                  body_type='{self.body_type}',body='{self.body}', content='{self.content}', 
                  files='{self.files}', params='{self.params}', headers='{self.headers}', 
                  cookies='{self.cookies}', timeout='{self.timeout}', expected_result='{self.expected_result}'
            )>
        """

    @classmethod
    def dumps_data(cls, data: dict):
        """
        如果为真则转换成json数据并返回,否则直接返空
        @param  :
        @return  :
        """
        return dumps(data, ensure_ascii=False, cls=CustomJSONEncoder) if data else data
