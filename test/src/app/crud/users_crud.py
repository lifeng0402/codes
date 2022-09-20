#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/20 20:17
# @Author  : debugfeng
# @Site    : 
# @File    : users_crud.py
# @Software: PyCharm

from sqlalchemy.orm import Session
from src.app.models import users_model
from src.app.schemas.users import user_schemas


class UsersCrud:

    def __init__(self, db: Session):
        self._db = db

    def create_user(self, user: user_schemas.UserPwd):
        """
        创建新用户，填入数据库
        :param user:
        :return: 
        """
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = users_model.Users(usename=user.username, password=fake_hashed_password)
        self._db.add(db_user)
        self._db.refresh(db_user)
        return db_user
