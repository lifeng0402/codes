#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: login.py
@时间: 2023/06/06 08:28:12
@说明: 
"""

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.orm import Session
from src.app.crud.users_crud import UsersCrud
from src.app.core.db.session import session
from src.app.core.base_redis import redis_client
from src.app.schemas.users_schemas import UsersLogin
from src.app.core.code_response import CodeResponse
from src.app.core.access_token import AccessToken


router = APIRouter(
    prefix="/users"
)


@router.post("/login")
async def user_login(users: UsersLogin, db: Session = Depends(session)):
    """
    登录接口
    @param  :
    @return  :
    """
    try:
        response = UsersCrud(session=db).login_user(user=users)
        if not response:
            raise

        access_token = AccessToken.token_encrypt(data=users)
        await redis_client.set(f"access_token:{users.username}", access_token)

        return CodeResponse.succeed(
            data=dict(response, **{"token": access_token})
        )
    except Exception as exc:
        return CodeResponse.defeated(
            err_msg=str(exc.args[0]),
            err_code=status.HTTP_503_SERVICE_UNAVAILABLE
        )
