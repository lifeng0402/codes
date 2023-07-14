#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: request.py
@时间: 2023/06/12 17:11:54
@说明:
"""

import json
from fastapi import APIRouter
from fastapi import Depends
from httpx import AsyncClient
from src.app.schemas.case import RequestBase
from src.app.core.code_response import CodeResponse
from src.app.core.dependencies import DependenciesProject


router = APIRouter(
    prefix="/request",
    dependencies=[Depends(DependenciesProject.dependence_token)]
)


@router.post("/send")
async def cases_resuest(datas: RequestBase):
    """
    单个请求接口
    @param  :
    @return  :
    """
    try:
        async with AsyncClient(verify=False) as asynclent:
            # 请求参数
            req_params = dict(
                url=datas.url, method=datas.method.upper(),
                json=datas.json_data, data=datas.form_data, params=datas.params,
                files=datas.files, content=datas.content, headers=datas.headers,
                cookies=datas.cookies, timeout=datas.timeout
            )
            # 开始请求
            request = await asynclent.request(**req_params)

            try:
                # 获取json返回值
                return request.json()
            except json.JSONDecodeError:
                return request.text

    except Exception as exc:
        return await CodeResponse.defeated(
            err_msg=str(exc.args)
        )
