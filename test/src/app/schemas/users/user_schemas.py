#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/20 20:07
# @Author  : debugfeng
# @Site    : 
# @File    : user_schemas.py
# @Software: PyCharm

from typing import Union
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserPwd(UserBase):
    password: str
