#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: request.py
@时间: 2023/06/12 17:11:54
@说明:
"""

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from src.app.core.access_token import AccessToken
from src.app.core.code_response import CodeResponse
from src.app.core.http_request import SafeRequest
from src.app.schemas.cases_schemas import RequestSchemas


router = APIRouter(
    #     dependencies=[Depends(AccessToken.verify_token)]
)


@router.post("/request")
async def cases_resuest(datas: RequestSchemas):
    try:
        return await SafeRequest.safe_request(datas=datas, is_response=True)
    except Exception as exc:
        return await CodeResponse.defeated(
            err_msg=str(exc.args),
            err_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )
