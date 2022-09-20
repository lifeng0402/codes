#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 10:33
# @Author  : debugfeng
# @Site    : 
# @File    : user.py
# @Software: PyCharm

from fastapi import APIRouter

router = APIRouter(prefix="/user")


@router.post("/register")
async def register_user():
    pass
