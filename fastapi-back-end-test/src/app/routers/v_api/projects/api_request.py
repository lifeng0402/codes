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
from src.app.core.access_token import AccessToken
from src.app.core.code_response import CodeResponse
from src.app.core.http_request import safe_request
from src.app.schemas.case import RequestSchemas


router = APIRouter(
    #     dependencies=[Depends(AccessToken.verify_token)]
)


@router.post("/request")
async def cases_resuest(datas: RequestSchemas):
    try:
        return await safe_request(
            method=datas.method, url=datas.url,
            body_type=datas.body_type, body=datas.body,
            params=datas.params, headers=datas.headers,
            cookies=datas.cookies, files=datas.files,
            timeout=datas.timeout, is_response=True
        )
    except Exception as exc:
        return await CodeResponse.defeated(
            err_msg=str(exc.args)
        )
