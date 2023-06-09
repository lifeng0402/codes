#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: users.py
@时间: 2023/05/31 19:25:00
@说明: 
"""

from pydantic import BaseModel, EmailStr


class UsersSchemas(BaseModel):
    mobile: str
    username: str
    password: str
    mailbox: EmailStr


class UserToken(BaseModel):
    username: str
    token: str


class UsersLogin(BaseModel):
    username: str
    password: str
