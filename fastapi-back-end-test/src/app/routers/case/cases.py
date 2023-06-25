#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: cases.py
@时间: 2023/06/16 13:53:19
@说明: 
"""

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from sqlalchemy.orm import Session
from src.app.core.db.session import session
from src.app.crud.cases_crud import CasesCrud
from src.app.core.code_response import CodeResponse
from src.app.schemas.cases_schemas import (
    RequestSchemas, DeleteCases
)


router = APIRouter(
    prefix="/cases",
    #     dependencies=[Depends(AccessToken.verify_token)]
)


@router.post("/save")
async def save_case(data: RequestSchemas, db: Session = Depends(session)):
    try:
        response = CasesCrud(db).save_cases(data)

        if not response:
            return HTTPException(detail=response)

        return CodeResponse.succeed(
            data=response, err_msg="添加成功"
        )
    except Exception as e:
        return CodeResponse.defeated(
            err_msg=str(e.args)
        )


@router.put("/{case_id}")
async def update_case(case_id: int, data: RequestSchemas, db: Session = Depends(session)):
    try:
        response = CasesCrud(db).update_cases(case_id, data)

        if not response:
            return HTTPException(detail=response)

        return CodeResponse.succeed(
            data=response, err_msg="添加成功"
        )
    except Exception as e:
        return CodeResponse.defeated(
            err_msg=str(e.args)
        )


@router.get("/list")
async def list_case(skip: int = 0, limit: int = 10, db: Session = Depends(session)):
    try:
        response = CasesCrud(db).case_list(skip=skip, limit=limit)
        return CodeResponse.succeed(data=response)
    except Exception as e:
        return CodeResponse.defeated(
            err_msg=str(e.args)
        )


@router.delete("/{case_id}")
async def delete_case(case_id: int, db: Session = Depends(session)):
    try:
        response, message = CasesCrud(db).case_delete(case_id=case_id)
        return CodeResponse.succeed(data=response, err_msg=message)
    except Exception as e:
        return CodeResponse.defeated(
            err_msg=str(e.args)
        )


@router.put("/batch")
async def batch_delete_case(case_id: DeleteCases, db: Session = Depends(session)):
    try:
        response, message = CasesCrud(db).case_batch_delete(case_id=case_id)
        return CodeResponse.succeed(data=response, err_msg=message)
    except Exception as e:
        return CodeResponse.defeated(
            err_msg=str(e.args)
        )
