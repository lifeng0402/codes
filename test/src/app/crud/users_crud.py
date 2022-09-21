#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/20 20:17
# @Author  : debugfeng
# @Site    : 
# @File    : users_crud.py
# @Software: PyCharm

from sqlalchemy import select
from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.app.models import users_model
from src.app.public.logger import do_logger
from src.app.schemas.users import user_schemas


class DatabasesUsers:

    def __init__(self, *, db: Session):
        self._session = db
        self._users = users_model.Users

    def create_users(self, *, user: user_schemas.UserPwd):
        """
        创建新用户，写入数据库Users表中
        :param user:
        :return: 
        """

        try:
            # 查询用户是否存在
            users_info = self._session.execute(
                select(self._users).where(self._users.username == user.username)
            )
            # 如果用户存在则抛出异常
            if users_info.scalars().first():
                raise Exception("用户已存在 ！")

            # 对密码进行加密处理
            fake_hashed_password = user.password + "notreallyhashed"
            db_users = self._users(username=user.username, password=fake_hashed_password)
            # 添加用户数据
            self._session.add(db_users)
            # 提交用户数据
            self._session.commit()
            # 刷新用户数据
            self._session.refresh(db_users)
            return db_users
        except Exception as e:
            do_logger.error(f"用户注册失败: {str(e)}")
            raise Exception("用户注册失败 ！")

    def get_info_users(self, *, username: str):
        """
        Users表中查询用户并返回
        :param username:
        :return:
        """
        db_users = self._session.execute(
            select(
                self._users.id,
                self._users.username,
                self._users.is_active
            ).where(self._users.username == username).first()
        )
        return db_users
