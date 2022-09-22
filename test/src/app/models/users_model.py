#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/20 11:50
# @Author  : debugfeng
# @Site    : 
# @File    : users_model.py
# @Software: PyCharm

from src.app.models import *

__all__ = ["Users", "Items"]


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, index=True, nullable=False)
    password = Column(String(200), nullable=False)
    mobile = Column(String(12), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    created_time = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated_time = Column(TIMESTAMP, nullable=False, default=datetime.now())

    items = relationship("Items", back_populates="users")


class Items(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    mail = Column(String(64), unique=True, index=True, nullable=False)
    brief_introduction = Column(String(200))
    created_time = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated_time = Column(TIMESTAMP, nullable=False, default=datetime.now())
    owner_id = Column(Integer, ForeignKey("users.id"))

    users = relationship("Users", back_populates="items")
