#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 10:33
# @Author  : debugfeng
# @Site    : 
# @File    : user.py
# @Software: PyCharm


from fastapi import status
from fastapi import Depends
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import BackgroundTasks
from src.app.public.redispy import redispy
from src.app.handler.fatcory import TestResponse
from src.app.public.databases import session_local
from src.app.crud.users_crud import DatabasesUsers
from src.app.schemas.users.user_schemas import UserPwd
from src.app.dependencies.access_token import AccessToken

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
        data = databases_users.register_users(user=user)
        if status.HTTP_200_OK and data:
            return TestResponse.successful(code=status.HTTP_200_OK, msg="注册成功，请登录 ！", data=data)
    except Exception as e:
        return TestResponse.defeated(code=status.HTTP_400_BAD_REQUEST, msg=str(e.args[0]), data={})


@router.post("/login")
async def login_user(user: UserPwd, background_tasks: BackgroundTasks, db: Session = Depends(session_local)):
    """
    登录接口
    :param user:
    :param background_tasks:
    :param db:
    :return:
    """
    try:
        databases_users = DatabasesUsers(db=db)
        if databases_users.login_users(user=user):
            token, expire = AccessToken.generate_access_token(data={"username": user.username},)

        # 后台运行写入token到redis数据库
        background_tasks.add_task(redispy.set_value, user.username, token, is_data=True)

        return TestResponse.successful(
            data=dict(username=user.username, expire=expire, token=token),
            code=status.HTTP_201_CREATED,
            msg="登录成功 ！"
        )
    except Exception as e:
        return TestResponse.defeated(code=status.HTTP_401_UNAUTHORIZED, msg=str(e.args[0]), data={})
