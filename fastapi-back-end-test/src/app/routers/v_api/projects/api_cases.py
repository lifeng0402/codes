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
    Depends
)
from sqlalchemy.orm import Session
from src.app.schemas.case import (
    RequestSchemas, DeleteCases
)
from src.app.core.database.session import session
from src.app.crud.crud_case import CasesCrud
from src.app.core.code_response import CodeResponse
from src.app.core.dependencies import DependenciesProject
from src.app.core.excpetions import DebugTestException


router = APIRouter(
    prefix="/case",
    # dependencies=[Depends(DependenciesProject.dependence_token)]
)


@router.post("/create")
async def create_case(data: RequestSchemas, db: Session = Depends(session)):
    """
    创建测试用例接口

    :param data: 请求参数
    :type data: RequestSchemas
    :param db: 依赖注入, defaults to Depends(session)
    :type db: Session, optional
    :return: 
    :rtype: json
    """
    try:
        response = CasesCrud(db).create_cases(data)
        return CodeResponse.succeed(
            data=response, err_msg="添加成功..."
        )
    except DebugTestException as e:
        return CodeResponse.defeated(err_msg=e.message)


@router.put("/{case_id}")
async def update_case(case_id: int, data: RequestSchemas, db: Session = Depends(session)):
    """
    编辑测试用例接口

    :param case_id: 测试用例ID
    :type case_id: int
    :param data: 请求参数
    :type data: RequestSchemas
    :param db: 依赖注入, defaults to Depends(session)
    :type db: Session, optional
    :return: 
    :rtype: json
    """
    try:
        response = CasesCrud(db).update_cases(case_id, data)
        return CodeResponse.succeed(
            data=response, err_msg="修改成功..."
        )
    except DebugTestException as e:
        return CodeResponse.defeated(err_msg=e.message)


@router.get("/list")
async def list_case(skip: int = 0, limit: int = 10, db: Session = Depends(session)):
    """
    测试用例列表接口

    :param skip: 页码, defaults to 0
    :type skip: int
    :param limit: 条数, defaults to 10
    :type limit: int
    :param db: 依赖注入, defaults to Depends(session)
    :type db: Session, optional
    :return: 
    :rtype: json
    """
    try:
        response = CasesCrud(db).case_list(skip=skip, limit=limit)
        return CodeResponse.succeed(
            data=response, err_msg="查询成功..."
        )
    except DebugTestException as e:
        return CodeResponse.defeated(err_msg=e.message)


@router.delete("/{case_id}")
async def delete_case(case_id: int, db: Session = Depends(session)):
    """
    删除测试用例接口

    :param case_id: 测试用例ID
    :type case_id: int
    :param db: 依赖注入, defaults to Depends(session)
    :type db: Session, optional
    :return: 
    :rtype: json
    """
    try:
        response = CasesCrud(db).case_delete(case_id=case_id)
        return CodeResponse.succeed(
            data=response, err_msg="删除成功..."
        )
    except DebugTestException as e:
        return CodeResponse.defeated(err_msg=e.message)


@router.post("/batch")
async def batch_delete_case(case: DeleteCases, db: Session = Depends(session)):
    """
    批量删除测试用例接口

    :param case: 请求参数
    :type case: DeleteCases
    :param db: 依赖注入, defaults to Depends(session)
    :type db: Session, optional
    :return: 
    :rtype: json
    """
    try:
        response = CasesCrud(db).case_batch_delete(case=case)
        return CodeResponse.succeed(
            data=response, err_msg="批量删除成功..."
        )
    except DebugTestException as e:
        return CodeResponse.defeated(err_msg=e.message)
