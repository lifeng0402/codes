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
    ForeignKey
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
from src.app.models.plan_models import Plan
from src.app.excpetions.datetime_excpetions import DateTimeEncoder


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

    cases = relationship("Plan", backref="cases", lazy="dynamic")

    def __repr__(self):
        return f"""
            <Cases(
                  id='{self.id}', method='{self.method}', url='{self.url}', 
                  body_type='{self.body_type}',body='{self.body}', content='{self.content}', 
                  files='{self.files}', params='{self.params}', headers='{self.headers}', 
                  cookies='{self.cookies}', timeout='{self.timeout}', auth='{self.auth}',
                  follow_redirects='{self.follow_redirects}', extensions='{self.extensions}', 
                  expected_result='{self.expected_result}'
            )>
        """

    def as_dict(self):
        # 定义个字空字典
        resutls_dicts = {}
        # 循环表中的字段
        for c in self.__table__.columns:
            # 判断值是否为空
            if getattr(self, c.name) is not None:
                # 往字典中更新数据
                resutls_dicts.update({c.name: getattr(self, c.name)})
                # 如果数据为时间类型
                if isinstance(getattr(self, c.name), datetime):
                    # 把时间格式化后转成字典并更新到字典中
                    resutls_dicts.update(
                        loads(
                            dumps(
                                {c.name: getattr(self, c.name)},
                                cls=DateTimeEncoder
                            )
                        )
                    )
            # 跳出本次循环
            continue
        # 返回一个新字典
        return resutls_dicts
