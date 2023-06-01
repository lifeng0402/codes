#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: users.py
@时间: 2023/05/31 20:18:18
@说明: 
"""

from sqlalchemy.orm import Session
from src.app.models.users_models import Users
from src.app.schemas.users_schemas import UsersSchemas
from sqlalchemy import (
    select,
    and_,
    or_
)

__all__ = [
    "UsersCrud"
]


class UsersCrud:
    def __init__(self, *, session: Session) -> None:
        self.db = session

    def register_user(self, user: UsersSchemas):
        """
        注册接口数据和数据库交互
        @param  :
        @return  :
        """
        try:
            # 首先查询手机号或者账号是否重复
            results = self.db.execute(
                select(Users.mobile, Users.username).where(
                    or_(
                        Users.mobile == user.mobile,
                        Users.username == user.username
                    )
                )
            )

            if results.scalars().first():
                raise Exception("账号或手机号重复....")

            users_info = Users(
                mobile=user.mobile, username=user.username,
                password=user.password, mailbox=user.mailbox
            )
            self.db.add(users_info)
            self.db.commit()
            self.db.refresh(users_info)

            # 查询新注册的账号信息
            update_results = self.db.execute(
                select(Users.id, Users.mobile, Users.username, Users.mailbox).where(
                    and_(
                        Users.mobile == user.mobile,
                        Users.username == user.username
                    )
                )
            ).first()
            return update_results
        except Exception as exc:
            raise exc
