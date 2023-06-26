#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: plan.py
@时间: 2023/06/20 19:04:15
@说明: 
"""

from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException
)
from sqlalchemy.orm import Session
from src.app.core.db.session import session
from src.app.crud.plan_crud import PlanCrud
from src.app.core.code_response import CodeResponse
from src.app.schemas.plan_schemas import PlanSchemas


router = APIRouter(
    prefix="/plan",
    #     dependencies=[Depends(AccessToken.verify_token)]
)


@router.post("/create")
async def plan_create(data: PlanSchemas, db: Session = Depends(session)):
    try:
        response = PlanCrud(db).create_plan(data)

        if not response:
            return HTTPException(detail=response)

        return CodeResponse.succeed(
            data=response, err_msg="添加成功"
        )
    except Exception as e:
        return CodeResponse.defeated(
            err_msg=str(e.args),
        )


@router.get("/list")
async def plan_list(skip: int = 0, limit: int = 10, db: Session = Depends(session)):
    try:
        response = PlanCrud(db).list_plan(skip=skip, limit=limit)

        if not response:
            return HTTPException(detail=response)

        return CodeResponse.succeed(
            data=response, err_msg="操作成功"
        )
    except Exception as e:
        return CodeResponse.defeated(
            err_msg=str(e.args),
        )
