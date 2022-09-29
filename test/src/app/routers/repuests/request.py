#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 18:03
# @Author  : debugfeng
# @Site    : 
# @File    : request.py
# @Software: PyCharm
import json

from fastapi import Depends
from fastapi import APIRouter
from sqlalchemy.orm import Session
from src.app.handler.client import HttpRequest
from src.app.crud.http_crud import DatabasesHttp
from src.app.handler.fatcory import TestResponse
from src.app.public.databases import session_local
from src.app.schemas.http.http_schemas import HttpBody, HttpBodySave
from src.app.dependencies.access_token import AccessToken

router = APIRouter(
    prefix="/http",
    # dependencies=[Depends(AccessToken.verify_token)]
)


@router.post("/save")
async def request_data_save(datas: HttpBodySave, db: Session = Depends(session_local)):
    """
    存储请求参数接口
    :param datas:
    :param db:
    :return:
    """
    try:
        databases_datas = DatabasesHttp(db=db)
        data = databases_datas.request_save_http(data=datas)
        return TestResponse.successful(msg="请求数据添加成功 ！", data=data)
    except Exception as ex:
        return TestResponse.defeated(msg=str(ex.args[0]))


@router.post("/request")
async def request_http(data: HttpBody):
    """
    请求HTTP协议接口
    :param data:
    :return:
    """
    try:
        response = HttpRequest().request(
            method=data.method, url=data.url, body=data.body,
            params=data.params, cookies=data.cookies, headers=data.headers, body_type=data.body_type
        )
        return TestResponse.successful(response=response)
    except Exception as ex:
        return TestResponse.defeated(msg=str(ex.args[0]))
