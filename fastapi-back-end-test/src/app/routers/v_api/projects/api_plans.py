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
from src.app.crud.crud_plan import PlanCrud
from src.app.core.code_response import CodeResponse
from src.app.schemas.plan import PlanSchemas
from src.app.core.dependencies import DependenciesProject


router = APIRouter(
    prefix="/plan",
        dependencies=[Depends(DependenciesProject.dependence_token)]
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


@router.put("/{plan_id}")
async def plan_update(plan_id: int, data: PlanSchemas, db: Session = Depends(session)):
    try:
        response = PlanCrud(db).update_plan(plan_id, data)

        return CodeResponse.succeed(
            data=response, err_msg="修改成功"
        )
    except Exception as e:
        return CodeResponse.defeated(
            err_msg=str(e.args)
        )


@router.get("/list")
async def plan_list(skip: int = 0, limit: int = 10, db: Session = Depends(session)):
    try:
        response = PlanCrud(db).list_plan(skip=skip, limit=limit)

        return CodeResponse.succeed(
            data=response, err_msg="查询成功"
        )
    except Exception as e:
        return CodeResponse.defeated(
            err_msg=str(e.args),
        )


@router.delete("/{plan_id}")
async def plan_list(plan_id: int, db: Session = Depends(session)):
    try:
        response = PlanCrud(db).delete_plan(plan_id)

        return CodeResponse.succeed(
            data=response, err_msg="删除成功"
        )
    except Exception as e:
        return CodeResponse.defeated(
            err_msg=str(e.args),
        )
