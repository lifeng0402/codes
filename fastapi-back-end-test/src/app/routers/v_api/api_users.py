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
    UseRregister, UsersLogin, UserLogout
)
from src.app.core.db.session import session
from src.app.crud.crud_user import UsersCrud
from src.app.core.code_response import CodeResponse


router = APIRouter(
    prefix="/user"
)


@router.post("/register")
async def user_register(users: UseRregister, db: Session = Depends(session)):
    """
    注册接口
    @param  :
    @return  :
    """
    try:
        response = UsersCrud(session=db).register(user=users)
        return CodeResponse.succeed(data=response)
    except Exception as exc:
        return CodeResponse.defeated(err_msg=str(exc.args[0]))


@router.post("/login")
async def user_login(users: UsersLogin, db: Session = Depends(session)):
    """
    登录接口
    @param  :
    @return  :
    """
    try:
        response = await UsersCrud(session=db).login(user=users)
        return CodeResponse.succeed(data=response)

    except Exception as exc:
        return CodeResponse.defeated(err_msg=str(exc.args))


@router.delete("/logout/{user_id}")
async def user_logout(user_id: UserLogout, db: Session = Depends(session)):
    """
    登出接口
    @param  :
    @return  :
    """
    try:
        response = await UsersCrud(session=db).logout(user=user_id)
        return CodeResponse.succeed(data=response)

    except Exception as exc:
        return CodeResponse.defeated(err_msg=str(exc.args))
