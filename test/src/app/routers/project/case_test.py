#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 15:50
# @Author  : debugfeng
# @Site    : 
# @File    : case_test.py
# @Software: PyCharm
import json

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from src.app.handler.fatcory import TestResponse
from src.app.public.databases import session_local
from src.app.schemas.project import cases_schemas
from src.app.crud import project_crud
from src.app.constructor.execute_run import ExecuteRun
from src.app.dependencies.access_token import AccessToken

router = APIRouter(
    prefix="/cases",
    # dependencies=[Depends(AccessToken.verify_token)]
)


@router.post("/add")
async def case_add(case: cases_schemas.CaseAdd, db: Session = Depends(session_local)):
    """
    存储请求参数接口
    :param case:
    :param db:
    :return:
    """
    try:
        databases_datas = project_crud.DatabasesCases(db=db)
        data = databases_datas.cases_add(case=case)
        return TestResponse.successful(msg="请求数据添加成功 ！", data=data)
    except Exception as ex:
        return TestResponse.defeated(msg=str(ex.args[0]))


@router.get("/case")
async def case_list(skip: int = 0, limit: int = 10, db: Session = Depends(session_local)):
    """
    用例列表
    :return:
    """
    try:
        databases_datas = project_crud.DatabasesCases(db=db)
        datas = databases_datas.cases_list(skip=skip, limit=limit)
        return TestResponse.successful(msg="查询数据成功", data=datas)
    except Exception as ex:
        TestResponse.defeated(msg=str(ex.args[0]))


@router.post("/execute")
async def case_execute(case: cases_schemas.CaseDatas, db: Session = Depends(session_local)):
    """
    批量执行用例接口
    :param case:
    :param db:
    :return:
    """
    try:
        databases_datas = project_crud.DatabasesCases(db=db)
        datas = databases_datas.cases_data(case=case)
        print(ExecuteRun().execute(response=datas), 323232)
        return TestResponse.successful(msg="查询数据成功", data=datas)
    except Exception as ex:
        TestResponse.defeated(msg=str(ex.args[0]))
