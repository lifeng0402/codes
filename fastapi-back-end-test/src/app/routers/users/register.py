#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: register.py
@时间: 2023/05/31 19:20:38
@说明: 
"""

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from src.app.crud.users_crud import UsersCrud
from src.app.public.db.session import session
from src.app.schemas.users_schemas import UsersSchemas


router = APIRouter(
    prefix="/users"
)


@router.post("/register")
async def user_register(users: UsersSchemas, db: Session = Depends(session)):
    """
    注册接口
    @param  :
    @return  :
    """
    return UsersCrud(session=db).register_user(user=users)
