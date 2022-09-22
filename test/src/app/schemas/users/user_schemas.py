#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/20 20:07
# @Author  : debugfeng
# @Site    : 
# @File    : user_schemas.py
# @Software: PyCharm

from typing import Union
from pydantic import BaseModel
from pydantic import validator, validators


class UserBase(BaseModel):
    mobile: str
    username: str

    @classmethod
    @validator('mobile', 'username')
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ValueError("不能为空")
        return v

    def __repr__(self):
        return self.username, self.mobile


class UserPwd(UserBase):
    password: str

    @classmethod
    @validator('password')
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ValueError("不能为空")
        return v

    def __repr__(self):
        return self.password
