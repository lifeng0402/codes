#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/29 15:04
# @Author  : debugfeng
# @Site    : 
# @File    : project_crud.py
# @Software: PyCharm

import json
import typing
from sqlalchemy.orm import Session
from src.app.models import case_model
from src.app.public.logger import do_logger
from src.app.schemas.project import cases_schemas
from src.app.enumeration.request_enum import BodyType
from src.app.public.databases import database_commit
from sqlalchemy import select, and_, or_

__all__ = ["DatabasesCases"]


class DatabasesCases:
    def __init__(self, *, db: Session):
        self._session = db
        self._cases = case_model.Cases

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

    @classmethod
    def _is_json(cls, *, results: typing.Any):
        data_list = []
        for data in results:
            results = dict(zip(data.keys(), data))
            results["datas"] = json.loads(results["datas"])
            data_list.append(results)
        return data_list

    def cases_add(self, *, case: cases_schemas.CaseAdd):
        """
        添加用例，新增到cases表中
        :param case:
        :return:
        """

        try:
            # 查询数据是否存在
            datas_info = self._session.execute(select(self._cases).where(self._cases.name == case.name))
            # 如果数据存在则抛出异常
            if datas_info.scalars().first():
                raise Exception(f"{case.name} - 名称已存在 ！")

            body_type = self._body_type_value_mode(body_type=case.body_type)
            db_datas = self._cases(
                name=case.name, datas=json.dumps([
                    {
                        "method": case.method, "url": case.url, "headers": case.headers,
                        "body_type": body_type, "body": case.body, "params": case.params, "cookies": case.cookies,
                        "actual": case.actual, "expect": case.expect, "comparison": case.comparison
                    }
                ])
            )
            # 提交数据成功后执行刷新
            database_commit(_session=self._session, _datas=db_datas)

            results_info = self._session.execute(
                select([self._cases.id, self._cases.name, self._cases.datas, self._cases.actual, self._cases.expect])
            ).fetchall()

            return self._is_json(results=results_info)

        except Exception as ex:
            do_logger.error(f"用例数据添加失败: {str(ex)}")
            raise ex

    def cases_data(self, *, case: cases_schemas.CaseDatas):
        """
        根据ID查询数据，用于批量执行接口请求
        :param case:
        :return:
        """
        try:
            db_datas = self._session.execute(
                select(
                    self._cases.id, self._cases.name, self._cases.datas, self._cases.actual, self._cases.expect,
                    self._cases.comparison, self._cases.is_success, self._cases.is_error, self._cases.exception
                ).where(and_(self._cases.id.in_(case.case_id), self._cases.is_active == 0))
            ).fetchall()

            return self._is_json(results=db_datas)
            # return [dict(zip(data.keys(), data)) for data in db_datas]

        except Exception as ex:
            do_logger.error(f"未查询到指定数据: {ex}")
            raise ex

    def cases_list(self, *, skip: int, limit: int):
        """
        获取用例列表数据
        :param skip:
        :param limit:
        :return:
        """
        try:
            db_datas = self._session.execute(
                select(
                    [
                        self._cases.id, self._cases.name, self._cases.datas, self._cases.is_success,
                        self._cases.is_error
                    ]
                ).offset(skip).limit(limit)
            ).fetchall()

            return self._is_json(results=db_datas)

        except Exception as ex:
            do_logger.error(f"列表数据为空: {ex}")
            raise ex
