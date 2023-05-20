#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/20 20:17
# @Author  : debugfeng
# @Site    :
# @File    : users_crud.py
# @Software: PyCharm

from sqlalchemy.orm import Session
from sqlalchemy import select, and_
from src.app.models import usersModels
from src.app.public.logger import do_logger
from src.app.schemas import userSchemas
from src.app.public.operationalDatabase import databaseCommit
from src.app.dependencies.accessToken import AccessToken


class DatabasesUsers:

    def __init__(self, *, db: Session):
        self._session = db
        self._users = usersModels.Users

    def register_users(self, *, user: userSchemas.UserPwd):
        """
        创建新用户,写入数据库Users表中
        :param user:
        :return: 
        """

        try:
            # 查询用户是否存在
            users_info = self._session.execute(
                select(
                    self._users.username, self._users.mobile, self._users.is_active
                ).where(and_(self._users.username == user.username, self._users.mobile == user.mobile))
            )

            # 如果用户存在则抛出异常
            if users_info.scalars().first():
                raise Exception("用户名或手机号已存在!")

            # 对密码进行加密处理
            hashed_password = AccessToken.encryption_password(
                pwd=user.password
            )

            # 提交数据成功后执行刷新，并返回数据
            databaseCommit(
                _session=self._session, _datas=self._users(
                    username=user.username, password=hashed_password, mobile=user.mobile
                )
            )

            # 查询新注册的账号信息
            db_users = self._session.execute(
                select(
                    self._users.id, self._users.mobile, self._users.username,
                    self._users.is_active, self._users.created_time, self._users.updated_time,
                ).where(
                    and_(
                        self._users.username == user.username,
                        self._users.mobile == user.mobile,
                        self._users.is_active == 1
                    )
                )
            ).first()
            return db_users
        except Exception as e:
            do_logger.error(f"用户注册失败: {str(e)}")
            raise Exception("注册失败!")

    def login_users(self, *, user: userSchemas.UserPwd):
        """
        Users表中根据条件查询用户是否存在并返回查询到的数据
        :param user:
        :return:
        """
        try:

            # 根据输入的用户名和密码当作条件，进入数据库查询
            db_users = self._session.execute(
                select(self._users.password).where(
                    and_(
                        self._users.username == user.username,
                        self._users.mobile == user.mobile,
                        self._users.is_active == 1
                    )
                )
            ).first()

            exception_info = Exception("用户或密码错误!")
            # 用户不存在则抛出异常
            if not db_users:
                raise exception_info

            if not AccessToken.decode_password(pwd=user.password, hashed_password=db_users[0]):
                raise exception_info

            return True
        except Exception as e:
            do_logger.error(f"用户 {user.username} 登录失败：{e}")
            raise e
