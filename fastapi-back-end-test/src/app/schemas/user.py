#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: users.py
@时间: 2023/05/31 19:25:00
@说明: 
"""

from pydantic import BaseModel, EmailStr


__all__ = [
    "UseRregister",
    "UsersLogin",
    "UserLogout",
    "UserSignOut",
    "UserChangePwd"
]


class User(BaseModel):
    username: str
    password: str


class UseRregister(User):
    pass


class UsersLogin(User):
    pass


class UserLogout(BaseModel):
    user_id: int


class UserSignOut(UserLogout):
    pass


class UserChangePwd(UserLogout):
    password:str
