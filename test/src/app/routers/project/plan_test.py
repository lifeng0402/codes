#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 15:51
# @Author  : debugfeng
# @Site    : 
# @File    : plan_test.py
# @Software: PyCharm

from fastapi import APIRouter

router = APIRouter(
    prefix="/plan"
)


@router.post("/create")
def plan_create():
    pass


@router.post("/plan")
def plan_list():
    pass
