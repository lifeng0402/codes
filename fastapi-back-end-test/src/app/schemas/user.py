#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: users.py
@时间: 2023/05/31 19:25:00
@说明: 
"""

from pydantic import BaseModel


__all__ = [
    "UseRregister",
    "UsersLogin",
    "UserChangePwd"
]


class User(BaseModel):
    username: str
    password: str


class UseRregister(User):
    pass


class UsersLogin(User):
    pass


class UserChangePwd(BaseModel):
    user_id: int
    password: str
