#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 15:51
# @Author  : debugfeng
# @Site    : 
# @File    : plan.py
# @Software: PyCharm


from src.app.schemas.project import plan_schemas
from fastapi import Depends
from fastapi import APIRouter
from sqlalchemy.orm import Session
from src.app.crud import plan_crud
from src.app.handler.fatcory import TestResponse
from src.app.public.databases import session_local
from src.app.dependencies.access_token import AccessToken

router = APIRouter(
    prefix="/plan",
    # dependencies=[Depends(AccessToken.verify_token)]
)


@router.post("/add")
async def plan_create(plan: plan_schemas.PlanAdd, db: Session = Depends(session_local)):
    """
    新增测试计划
    :param plan:
    :param db:
    :return:
    """
    try:
        databases_datas = plan_crud.DatabasesPlan(db=db)
        data = databases_datas.plan_add(plan=plan)
        return TestResponse.successful(msg="测试计划添加成功 ！", data=data)
    except Exception as ex:
        return TestResponse.defeated(msg=str(ex.args[0]))


@router.get("/plan")
async def plan_list(skip: int = 0, limit: int = 10, db: Session = Depends(session_local)):
    """
    测试计划列表
    :param skip:
    :param limit:
    :param db:
    :return:
    """
    try:
        databases_datas = plan_crud.DatabasesPlan(db=db)
        data = databases_datas.plan_list(skip=skip, limit=limit)
        return TestResponse.successful(msg="数据查询成功 ！", data=data)
    except Exception as ex:
        return TestResponse.defeated(msg=str(ex.args[0]))
