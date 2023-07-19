#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: users.py
@时间: 2023/05/31 19:25:00
@说明: 
"""

from dataclasses import dataclass


__all__ = [
    "UseRregister",
    "UsersLogin",
    "UserChangePwd"
]


@dataclass
class User:
    username: str
    password: str


@dataclass
class UseRregister(User):
    pass


@dataclass
class UsersLogin(User):
    pass


@dataclass
class UserChangePwd:
    user_id: int
    password: str
