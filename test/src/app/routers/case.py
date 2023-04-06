#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 15:50
# @Author  : debugfeng
# @Site    : 
# @File    : case.py
# @Software: PyCharm


from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from src.app.utilClass.fatcory import TestResponse
from src.app.public.operationalDatabase import operDatabase
from src.app.schemas import casesSchemas
from src.app.crud import casesCrud
from src.app.constructor.execute import ExecuteRun
from src.app.dependencies.accessToken import AccessToken

router = APIRouter(
    prefix="/case",
    # dependencies=[Depends(AccessToken.verify_token)]
)


@router.post("/add")
async def case_add(case: casesSchemas.CaseAdd, db: Session = Depends(operDatabase)):
    """
    存储请求参数接口
    :param case:
    :param db:
    :return:
    """
    try:
        databases_datas = casesCrud.DatabasesCases(db=db)
        data = databases_datas.cases_add(case=case)
        return TestResponse.successful(msg="数据添加成功!", data=data)
    except Exception as ex:
        return TestResponse.defeated(msg=str(ex.args[0]))


@router.put("/update")
async def case_update(case: casesSchemas.CaseUpdate, db: Session = Depends(operDatabase)):
    """
    修改请求参数接口
    :param case:
    :param db:
    :return:
    """
    try:
        databases_datas = casesCrud.DatabasesCases(db=db)
        data = databases_datas.cases_update(case=case)
        return TestResponse.successful(msg="数据更新成功!", data=data)
    except Exception as ex:
        return TestResponse.defeated(msg=str(ex.args[0]))


@router.get("/cases")
async def case_list(skip: int = 0, limit: int = 10, db: Session = Depends(operDatabase)):
    """
    用例列表
    :return:
    """
    try:
        databases_datas = casesCrud.DatabasesCases(db=db)
        datas = databases_datas.cases_list(skip=skip, limit=limit)
        return TestResponse.successful(msg="查询数据成功", data=datas)
    except Exception as ex:
        TestResponse.defeated(msg=str(ex.args[0]))


@router.delete("/delete")
async def case_update(case: casesSchemas.CaseDatas, db: Session = Depends(operDatabase)):
    """
    删除请求参数接口
    :param case:
    :param db:
    :return:
    """
    try:
        databases_datas = casesCrud.DatabasesCases(db=db)
        data = databases_datas.cases_delete(case=case)
        if data is not None:
            raise
        return TestResponse.successful(msg="数据删除成功!")
    except Exception as ex:
        return TestResponse.defeated(msg=str(ex.args[0]))