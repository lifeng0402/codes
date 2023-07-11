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
from src.app.crud.crud_case import CasesCrud
from src.app.core.code_response import CodeResponse
from src.app.schemas.case import (
    RequestSchemas, DeleteCases, BatchTestCaseRequest
)
from src.app.core.execute_cases import Execute
from src.app.core.dependencies import DependenciesProject


router = APIRouter(
    prefix="/case",
        dependencies=[Depends(DependenciesProject.dependence_token)]
)


@router.post("/create")
async def create_case(data: RequestSchemas, db: Session = Depends(session)):
    """
    测试用例保存接口
    @param  :
    @return  :
    """
    try:
        response = CasesCrud(db).create_cases(data)

        return CodeResponse.succeed(
            data=response, err_msg="添加成功..."
        )
    except Exception as e:
        return CodeResponse.defeated(
            err_msg=str(e.args)
        )


@router.put("/{case_id}")
async def update_case(case_id: int, data: RequestSchemas, db: Session = Depends(session)):
    """
    编辑测试用例接口
    @param  :
    @return  :
    """
    try:
        response = CasesCrud(db).update_cases(case_id, data)
        return CodeResponse.succeed(
            data=response, err_msg="修改成功..."
        )
    except Exception as e:
        return CodeResponse.defeated(
            err_msg=str(e.args)
        )


@router.get("/list")
async def list_case(skip: int = 0, limit: int = 10, db: Session = Depends(session)):
    """
    测试用例列表接口
    @param  :
    @return  :
    """
    try:
        response = CasesCrud(db).case_list(skip=skip, limit=limit)
        return CodeResponse.succeed(
            data=response, err_msg="查询成功..."
        )
    except Exception as e:
        return CodeResponse.defeated(
            err_msg=str(e.args)
        )


@router.delete("/{case_id}")
async def delete_case(case_id: int, db: Session = Depends(session)):
    """
    删除单个用例接口
    @param  :
    @return  :
    """
    try:
        response = CasesCrud(db).case_delete(case_id=case_id)
        return CodeResponse.succeed(
            data=response, err_msg="删除成功..."
        )
    except Exception as e:
        return CodeResponse.defeated(
            err_msg=str(e.args)
        )


@router.post("/batch")
async def batch_delete_case(case: DeleteCases, db: Session = Depends(session)):
    """
    批量删除用例接口
    @param  :
    @return  :
    """
    try:
        response = CasesCrud(db).case_batch_delete(case=case)
        return CodeResponse.succeed(
            data=response, err_msg="批量删除成功..."
        )
    except Exception as e:
        return CodeResponse.defeated(
            err_msg=str(e.args)
        )


@router.post("/running")
async def run_test_cases(case_ids: BatchTestCaseRequest, db: Session = Depends(session)):
    """
    批量运行用例接口
    @param  :
    @return  :
    """
    try:
        response = CasesCrud(db).cases_running(case_ids=case_ids)
        results = await Execute.run(response)
        return CodeResponse.succeed(
            data=results, err_msg="批量运行成功..."
        )
    except Exception as e:
        return CodeResponse.defeated(
            err_msg=str(e.args)
        )
