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
from fastapi import status
from src.app.core.dependencies import DependenciesProject
from src.app.core.code_response import CodeResponse


router = APIRouter(
    dependencies=[Depends(DependenciesProject.verify_token)]
)


@router.get("/index")
async def home_index():
    try:
        result = CodeResponse.succeed(
            data=dict(info="Welcome to the home page")
        )
        return result
    except Exception as exc:
        return CodeResponse.defeated(
            err_msg=str(exc.args[0]),
            err_code=status.HTTP_503_SERVICE_UNAVAILABLE
        )
