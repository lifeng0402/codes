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
    HTTPException
)
from sqlalchemy.orm import Session
from src.app.schemas.plan import (
    PlanSchemas, PlanExcute
)
from src.app.core.db.session import session
from src.app.crud.crud_plan import PlanCrud
from src.app.core.execute_cases import ExecuteCase
from src.app.core.code_response import CodeResponse
from src.app.core.dependencies import DependenciesProject
from src.app.excpetions.debug_test import DebugTestException


router = APIRouter(
    prefix="/plan",
    # dependencies=[Depends(DependenciesProject.dependence_token)]
)


@router.post("/create")
async def plan_create(data: PlanSchemas, db: Session = Depends(session)):
    """
    新建测试计划接口
    
    :param data: 请求参数
    :type data: dict
    :param db: 依赖注入, defaults to Depends(session)
    :type db: Session, optional
    :return: 
    :rtype: json
    """
    try:
        response = PlanCrud(db).create_plan(data)
        return CodeResponse.succeed(
            data=response, err_msg="添加成功"
        )
    except DebugTestException as e:
        return CodeResponse.defeated(err_msg=e.message)


@router.put("/{plan_id}")
async def plan_update(plan_id: int, data: PlanSchemas, db: Session = Depends(session)):
    """
    修改测试计划接口
    
    :param plan_id: 计划ID
    :type plan_id: int
    :param data: 请求参数
    :type data: PlanSchemas
    :param db: 依赖注入, defaults to Depends(session)
    :type db: Session, optional
    :return: 
    :rtype: json
    """
    try:
        response = PlanCrud(db).update_plan(plan_id, data)
        return CodeResponse.succeed(
            data=response, err_msg="修改成功"
        )
    except DebugTestException as e:
        return CodeResponse.defeated(err_msg=e.message)


@router.get("/list")
async def plan_list(skip: int = 0, limit: int = 10, db: Session = Depends(session)):
    """
    测试计划列表接口
    
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
        response = PlanCrud(db).list_plan(skip=skip, limit=limit)
        return CodeResponse.succeed(
            data=response, err_msg="查询成功"
        )
    except DebugTestException as e:
        return CodeResponse.defeated(err_msg=e.message)


@router.delete("/{plan_id}")
async def plan_delete(plan_id: int, db: Session = Depends(session)):
    """
    删除测试计划接口
    
    :param plan_id: 计划ID
    :type plan_id: int
    :param db: 依赖注入, defaults to Depends(session)
    :type db: Session, optional
    :return: 
    :rtype: json
    """
    try:
        response = PlanCrud(db).delete_plan(plan_id)
        return CodeResponse.succeed(
            data=response, err_msg="删除成功"
        )
    except DebugTestException as e:
        return CodeResponse.defeated(err_msg=e.message)


@router.post("/execute")
async def plan_execute(data: PlanExcute, db: Session = Depends(session)):
    """
    执行测试计划发送请求接口
    
    :param data: 请求参数
    :type data: PlanExcute
    :param db: 依赖注入, defaults to Depends(session)
    :type db: Session, optional
    :return: 
    :rtype: json
    """
    try:
        response = PlanCrud(db).execute_plan(data)
        response = await ExecuteCase.execute(response, db)
        return CodeResponse.succeed(
            data=response, err_msg=""
        )
    except DebugTestException as e:
        return CodeResponse.defeated(err_msg=e.message)
