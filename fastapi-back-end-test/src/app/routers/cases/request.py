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
from src.app.schemas.cases_schemas import RequestSchemas
from src.app.cabinet.code_response import CodeResponse
from src.app.public.send_request import RequestHttp


router = APIRouter(
    prefix="/cases",
    #     dependencies=[Depends(AccessToken.verify_token)]
)


@router.post("/request")
async def cases_resuest(datas: RequestSchemas):
    try:
        async with RequestHttp() as client:
            resutls = await client.safe_request(
                method=datas.method,
                url=datas.url,
                content=datas.content,
                data=datas.data,
                files=datas.files,
                json=datas.json_data,
                params=datas.params,
                headers=datas.headers,
                cookies=datas.cookies,
                timeout=datas.timeout,
                auth=datas.auth,
                follow_redirects=datas.follow_redirects,
                extensions=datas.extensions,
            )
            return resutls.json()
    except Exception as exc:
        return CodeResponse.defeated(
            err_msg=str(exc.args[0]),
            err_code=status.HTTP_400_BAD_REQUEST
        )
