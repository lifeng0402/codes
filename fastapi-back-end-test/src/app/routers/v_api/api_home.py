#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: index.py
@时间: 2023/06/09 08:28:00
@说明: 
"""


from fastapi import APIRouter
from fastapi import Depends
from fastapi import status, HTTPException
from src.app.core.dependencies import DependenciesProject
from src.app.core.code_response import CodeResponse
from src.app.excpetions.debug_test import DebugTestException


router = APIRouter(
    dependencies=[Depends(DependenciesProject.dependence_token)]
)


@router.get("/index")
async def home_index():
    try:
        result = CodeResponse.succeed(
            data=dict(info="Welcome to the home page")
        )
        return result
    except DebugTestException as e:
        return CodeResponse.defeated(err_msg=e.message)
