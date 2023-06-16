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
    status,
    HTTPException
)
from sqlalchemy.orm import Session
from src.app.core.db.session import session
from src.app.crud.cases_crud import CasesCrud
from src.app.core.code_response import CodeResponse
from src.app.schemas.cases_schemas import RequestSchemas


router = APIRouter(
    prefix="/cases",
    #     dependencies=[Depends(AccessToken.verify_token)]
)


@router.post("/save")
async def save_case(data: RequestSchemas, db: Session = Depends(session)):
    try:
        response = CasesCrud(db).save_cases(data)
        return CodeResponse.succeed(data=response)
    except Exception as e:
        return CodeResponse.defeated(
            err_msg=str([i for i in e.args]),
            err_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )
