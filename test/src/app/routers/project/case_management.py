#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 15:50
# @Author  : debugfeng
# @Site    : 
# @File    : case_management.py
# @Software: PyCharm
import json

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from src.app.handler.fatcory import TestResponse
from src.app.public.databases import session_local
from src.app.schemas.project.cases_schemas import CaseDatas
from src.app.crud.project_crud import DatabaseProject
from src.app.constructor.execute_run import ExecuteRun
from src.app.dependencies.access_token import AccessToken

router = APIRouter(
    prefix="/cases",
    # dependencies=[Depends(AccessToken.verify_token)]
)


@router.post("/execute")
def case_execute(cases: CaseDatas, db: Session = Depends(session_local)):
    try:
        databases_datas = DatabaseProject(db=db)
        datas = databases_datas.cases_data(case=cases)
        print(ExecuteRun().execute(datas=datas), 323232)
        return TestResponse.successful(msg="查询数据成功", data=datas)
    except Exception as ex:
        TestResponse.defeated(msg=str(ex.args[0]))
