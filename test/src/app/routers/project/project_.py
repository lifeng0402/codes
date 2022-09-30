#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 15:31
# @Author  : debugfeng
# @Site    : 
# @File    : project_.py
# @Software: PyCharm

from fastapi import APIRouter

router = APIRouter(
    prefix="/project"
)


@router.post("/create")
def project_create():
    pass


@router.post("/project")
def project_list():
    pass
