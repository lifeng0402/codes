#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/20 11:50
# @Author  : debugfeng
# @Site    : 
# @File    : users_model.py
# @Software: PyCharm

from src.app.models import *

__all__ = ["Users", "Items"]


class Users(BASE):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(50))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Items(BASE):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    description = Column(String(200), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
