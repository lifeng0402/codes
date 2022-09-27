#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/27 20:21
# @Author  : debugfeng
# @Site    : 
# @File    : http_crud.py
# @Software: PyCharm

from sqlalchemy import select, and_
from sqlalchemy.orm import Session
from src.app.models import datas_model
from src.app.public.logger import do_logger
from src.app.schemas.http import http_schemas
from src.app.dependencies.access_token import AccessToken


class DatabasesHttp:
    def __init__(self, *, db: Session):
        self._session = db
        self._datas = datas_model.Datas

    def request_save_http(self, *, data: http_schemas.HttpBody):
        try:
            db_users = self._datas(
                method=data.method, url=data.url, headers=data.headers, body_type=data.body_type, body=data.body
            )
            # 添加用户数据
            self._session.add(db_users)
            # 提交用户数据
            self._session.commit()
            # # 刷新用户数据
            self._session.refresh(db_users)
            return db_users
        except Exception as e:
            do_logger.error(f"用户注册失败: {str(e)}")
            raise Exception("注册失败 ！")
