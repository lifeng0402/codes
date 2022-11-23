#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/27 20:21
# @Author  : debugfeng
# @Site    : 
# @File    : http_crud.py
# @Software: PyCharm

from sqlalchemy import select
from sqlalchemy.orm import Session
from src.app.models import datas_model
from src.app.public.logger import do_logger
from src.app.schemas.http import http_schemas
from src.app.enumeration.request_enum import BodyType
from src.app.public.databases import database_commit


class DatabasesHttp:
    def __init__(self, *, db: Session):
        self._session = db
        self._datas = datas_model.Datas

    @classmethod
    def _body_type_value_mode(cls, *, body_type: BodyType):
        """
        判断类型并返回
        :param body_type:
        :return:
        """
        match body_type:
            case BodyType.form_data:
                return body_type.form_data.value
            case BodyType.form_urlencoded:
                return body_type.form_urlencoded.value
            case BodyType.binary:
                return body_type.binary.value
            case BodyType.json:
                return body_type.json.value
            case BodyType.graphQL:
                return body_type.graphQL.value
            case _:
                return body_type.none.value

    def request_save_http(self, *, data: http_schemas.HttpBodySave):
        """
        接口请求数据，新增到Datas表中
        :param data:
        :return:
        """

        try:
            # 查询数据是否存在
            datas_info = self._session.execute(select(self._datas).where(self._datas.title == data.title))
            # 如果数据存在则抛出异常
            if datas_info.scalars().first():
                raise Exception("title名称已存在 ！")

            body_type = self._body_type_value_mode(body_type=data.body_type)
            db_datas = self._datas(
                title=data.title, method=data.method, url=data.url, headers=str(data.headers),
                body_type=body_type, body=str(data.body), params=str(data.params),
                cookies=str(data.cookies), actual=str(data.actual), expect=str(data.expect)
            )
            # 提交数据成功后执行刷新, 并返回数据
            return database_commit(_session=self._session, _datas=db_datas)
        except Exception as ex:
            do_logger.error(f"数据添加失败: {str(ex)}")
            raise ex
