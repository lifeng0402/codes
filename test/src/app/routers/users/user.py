#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 10:33
# @Author  : debugfeng
# @Site    : 
# @File    : user.py
# @Software: PyCharm

import traceback
from fastapi import status
from fastapi import Depends
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from src.app.schemas.response.response_schemas import SrcResponse
from src.app.handler.fatcory import TestResponse
from src.app.public.databases import session_local
from src.app.crud.users_crud import DatabasesUsers
from src.app.schemas.users.user_schemas import UserPwd

router = APIRouter(
    prefix="/user",
)


@router.post("/register")
async def register_user(user: UserPwd, db: Session = Depends(session_local)):
    """
    注册接口
    :param user:
    :param db:
    :return:
    """

    try:
        databases_users = DatabasesUsers(db=db)
        data = databases_users.create_users(user=user)
        if status.HTTP_200_OK and data:
            return TestResponse.successful(code=status.HTTP_200_OK, msg="注册成功，请登录 ！", data=data)
    except Exception as e:
        return TestResponse.defeated(code=status.HTTP_400_BAD_REQUEST, msg=str(e.args[0]), data={})
