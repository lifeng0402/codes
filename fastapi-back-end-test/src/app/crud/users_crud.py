#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: users.py
@时间: 2023/05/31 20:18:18
@说明: 
"""


from sqlalchemy.orm import Session
from sqlalchemy import (
    select,
    and_,
    or_
)
from src.app.models.users_models import Users
from src.app.schemas.users_schemas import UsersLogin
from src.app.schemas.users_schemas import UsersSchemas
from src.app.public.verification import VerificationData

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

            # 验证手机号格式是否规范
            if not VerificationData.verification(mobile=user.mobile):
                raise Exception("手机号码格式不正确...")

            # 验证账号长度
            if not VerificationData.verification_lenth(var=user.username):
                raise Exception("账号长度为5-15个字符...")

            # 验证密码长度
            if not VerificationData.verification_lenth(var=user.password, max_len=25):
                raise Exception("密码长度为5-25个字符...")

            # 验证邮箱格式是否规范
            if not VerificationData.verification_email(email=user.mailbox):
                raise Exception("邮箱格式不正确...")

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
                raise Exception("账号或手机号重复...")

            # 接收到数据并赋值给users_info
            users_info = Users(
                mobile=user.mobile, username=user.username,
                password=user.password, mailbox=user.mailbox
            )
            # 往数据库添加数据
            self.db.add(users_info)
            # 往数据库提交数据
            self.db.commit()
            # 刷新提交的数据
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

    def login_user(self, user: UsersLogin):
        """
        登录接口查询数据并返回
        @param  :
        @return  :
        """

        def select_username(*, db: Session):
            results = db.execute(
                select(Users.id, Users.mobile, Users.username, Users.mailbox).where(
                    and_(
                        Users.password == user.password,
                        Users.username == user.username
                    )
                )
            )
            return results

        try:
            if not select_username(db=self.db).scalars().first():
                raise Exception("账号或密码错误...")

            return select_username(db=self.db).fetchone()
        except Exception as exc:
            raise exc
