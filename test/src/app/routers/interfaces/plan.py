#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 15:51
# @Author  : debugfeng
# @Site    : 
# @File    : plan.py
# @Software: PyCharm
import typing

from src.app.schemas import planSchemas
from fastapi import Depends
from fastapi import APIRouter
from sqlalchemy.orm import Session
from src.app.crud import planCrud
from src.app.utils.fatcory import TestResponse
from src.app.public.operationalDatabase import operDatabase
from src.app.dependencies.accessToken import AccessToken

router = APIRouter(
    prefix="/plan",
    dependencies=[Depends(AccessToken.verify_token)]
)


@router.post("/add")
async def plan_create(plan: planSchemas.PlanAdd, db: Session = Depends(operDatabase)):
    """
    新增测试计划
    :param plan:
    :param db:
    :return:
    """
    try:
        databases_datas = planCrud.DatabasesPlan(db=db)
        data = databases_datas.plan_add(plan=plan)
        return TestResponse.successful(msg="添加成功!", data=data)
    except Exception as ex:
        return TestResponse.defeated(msg=str(ex.args[0]))


@router.put("/update")
async def plan_update(plan: planSchemas.PlanUpdate, db: Session = Depends(operDatabase)):
    """
    修改测试计划
    :param plan:
    :param db:
    :return:
    """
    try:
        databases_datas = planCrud.DatabasesPlan(db=db)
        data = databases_datas.plan_update(plan=plan)
        return TestResponse.successful(msg="修改成功!", data=data)
    except Exception as ex:
        return TestResponse.defeated(msg=str(ex.args[0]))


@router.get("/plan")
async def plan_list(skip: int = 0, limit: int = 10, db: Session = Depends(operDatabase)):
    """
    测试计划列表
    :param skip:
    :param limit:
    :param db:
    :return:
    """
    try:
        databases_datas = planCrud.DatabasesPlan(db=db)
        data = databases_datas.plan_list(skip=skip, limit=limit)
        return TestResponse.successful(msg="查询成功!", data=data)
    except Exception as ex:
        return TestResponse.defeated(msg=str(ex.args[0]))


@router.delete("/delete/{plan_id}")
async def plan_delete(plan_id: int, db: Session = Depends(operDatabase)):
    """
    删除测试计划
    :param plan_id:
    :param db:
    :return:
    """
    try:
        databases_datas = planCrud.DatabasesPlan(db=db)
        data = databases_datas.plan_delete(plan_id=plan_id)
        return TestResponse.successful(msg="删除成功!", data=data)
    except Exception as ex:
        return TestResponse.defeated(msg=str(ex.args[0]))


@router.post("/cases")
async def plan_cases(case_id: planSchemas.PlanData, db: Session = Depends(operDatabase)):
    pass


async def plan_execute(case_id: planSchemas.PlanData, db: Session = Depends(operDatabase)):
    """
    批量执行计划中的测试用例
    :param case_id:
    :param db:
    :return:
    """
    try:
        databases_datas = planCrud.DatabasesPlan(db=db)
        data = databases_datas.plan_execute(case_id=case_id)
        return TestResponse.successful(msg="用例运行完毕!", data=data)
    except Exception as ex:
        return TestResponse.defeated(msg=str(ex.args[0]))
