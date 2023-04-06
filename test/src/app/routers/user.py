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
from src.app.public.operationalRedis import redispy
from src.app.utilClass.fatcory import TestResponse
from src.app.public.operationalDatabase import operDatabase
from src.app.crud.usersCrud import DatabasesUsers
from src.app.schemas.userSchemas import UserPwd
from src.app.dependencies.accessToken import AccessToken

router = APIRouter(
    prefix="/user",
)


@router.post("/register", name="注册接口")
async def register_user(user: UserPwd, db: Session = Depends(operDatabase)):
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
            return TestResponse.successful(msg="注册成功，请登录!", data=data)
    except Exception as e:
        return TestResponse.defeated(msg=str(e.args[0]), data={})


@router.post("/login", name="登录接口")
async def login_user(user: UserPwd, background_tasks: BackgroundTasks, db: Session = Depends(operDatabase)):
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
            token, expire = AccessToken.generate_access_token(data={"username": user.username}, )

        # 后台运行写入token到redis数据库
        background_tasks.add_task(redispy.set_value, user.username, token, is_data=True)

        return TestResponse.successful(
            msg="登录成功 !",
            data=dict(username=user.username, expire=expire, token=token)
        )
    except Exception as e:
        return TestResponse.defeated(msg=str(e.args[0]), data={})

async def logout_user():
    pass