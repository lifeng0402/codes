#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: users.py
@时间: 2023/06/29 17:09:03
@说明: 
"""

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from src.app.schemas.user import (
    UseRregister,
    UsersLogin,
    UserChangePwd
)
from src.app.core.db.session import session
from src.app.crud.crud_user import UsersCrud
from src.app.core.code_response import CodeResponse
from src.app.excpetions.debug_test import DebugTestException


router = APIRouter(
    prefix="/user"
)


@router.post("/register")
async def user_register(users: UseRregister, db: Session = Depends(session)):
    """
    注册接口

    :param users: 请求参数
    :type users: UseRregister
    :param db: 依赖注入, defaults to Depends(session)
    :type db: Session, optional
    :return: 
    :rtype: json
    """
    try:
        response = UsersCrud(session=db).register(user=users)
        return CodeResponse.succeed(data=response)
    except DebugTestException as e:
        return CodeResponse.defeated(err_msg=e.message)


@router.post("/login")
async def user_login(users: UsersLogin, db: Session = Depends(session)):
    """
    登录接口

    :param users: 请求参数
    :type users: UsersLogin
    :param db: 依赖注入, defaults to Depends(session)
    :type db: Session, optional
    :return: 
    :rtype: json
    """
    try:
        response = await UsersCrud(session=db).login(user=users)
        return CodeResponse.succeed(data=response)

    except DebugTestException as e:
        return CodeResponse.defeated(err_msg=e.message)


@router.put("/password")
async def user_change_password(user: UserChangePwd, db: Session = Depends(session)):
    """
    修改密码接口

    :param user: 请求参数
    :type user: UserChangePwd
    :param db: 依赖注入, defaults to Depends(session)
    :type db: Session, optional
    :return: 
    :rtype: json
    """
    try:
        response = UsersCrud(session=db).change_password(user=user)
        return CodeResponse.succeed(data=response)

    except DebugTestException as e:
        return CodeResponse.defeated(err_msg=e.message)


@router.delete("/logout/{user_id}")
async def user_logout(user_id: int, db: Session = Depends(session)):
    """
    登出接口

    :param user_id: 用户ID
    :type user_id: int
    :param db: 依赖注入, defaults to Depends(session)
    :type db: Session, optional
    :return: 
    :rtype: json
    """
    try:
        response = await UsersCrud(session=db).logout(user_id=user_id)
        return CodeResponse.succeed(data=response)

    except DebugTestException as e:
        return CodeResponse.defeated(err_msg=e.message)


@router.delete("/signout/{user_id}")
async def user_sign_out(user_id: int, db: Session = Depends(session)):
    """
    注销登录接口

    :param user_id: 用户ID
    :type user_id: int
    :param db: 依赖注入, defaults to Depends(session)
    :type db: Session, optional
    :return: 
    :rtype: json
    """
    try:
        response = await UsersCrud(session=db).sign_out(user_id=user_id)
        return CodeResponse.succeed(data=response)

    except DebugTestException as e:
        return CodeResponse.defeated(err_msg=e.message)
