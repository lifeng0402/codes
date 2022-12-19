#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/29 15:04
# @Author  : debugfeng
# @Site    : 
# @File    : cases_crud.py
# @Software: PyCharm

import json
import typing
from sqlalchemy.orm import Session
from src.app.models import case_model
from src.app.public.logger import do_logger
from src.app.schemas.project import cases_schemas
from src.app.enumeration.request_enum import BodyType
from src.app.public.databases import database_commit
from sqlalchemy import select, and_, or_, update, delete

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
                        "body_type": body_type, "body": case.body, "params": case.params, "cookies": case.cookies
                    }
                ]), actual=case.comparison, expect=case.expect
            )
            # 提交数据成功后执行刷新
            database_commit(_session=self._session, _datas=db_datas)

            results_info = self._session.execute(
                select([self._cases.id, self._cases.name, self._cases.datas, self._cases.expect])
            ).fetchall()

            return self._cases.is_json(results=results_info)

        except Exception as ex:
            do_logger.error(f"用例数据添加失败: {str(ex)}")
            raise ex

    def cases_update(self, *, case: cases_schemas.CaseUpdate):
        """
        修改用例，更新到cases表中
        :param case:
        :return:
        """

        def select_(var1: typing.Any, var2: typing.Any):
            # 查询数据是否存在
            return self._session.execute(select(self._cases).where(var1 == var2)).scalars().first()

        try:
            # 如果数据不存在则抛出异常,存在则检查名称是否唯一
            datas = select_(self._cases.id, case.case_id)
            if not datas:
                raise Exception(f"数据不存在 ！")

            body_type = self._body_type_value_mode(body_type=case.body_type)

            # 执行数据更新操作
            datas_info = self._session.execute(
                update(self._cases).where(self._cases.id == case.case_id).values(
                    name=case.name, datas=json.dumps([
                        {
                            "method": case.method, "url": case.url, "headers": case.headers,
                            "body_type": body_type, "body": case.body, "params": case.params, "cookies": case.cookies
                        }
                    ]), expect=case.expect, comparison=case.comparison
                )
            )
            # 提交并更新数据库
            self._session.commit()
            self._session.refresh(datas_info)
            # 查询更新后的数据
            results_info = self._session.execute(
                select(
                    [self._cases.id, self._cases.name, self._cases.datas, self._cases.expect]
                ).where(self._cases.id == case.case_id)
            )

            return self._cases.is_json(results=results_info)

        except Exception as ex:
            do_logger.error(f"用例数据更新失败: {str(ex)}")
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
                        self._cases.is_error,
                        self._cases.actual, self._cases.expect, self._cases.exception, self._cases.comparison
                    ]
                ).where(self._cases.is_active == 0).offset(skip).limit(limit)
            ).all()

            return self._cases.is_json(results=db_datas)

        except Exception as ex:
            do_logger.error(f"列表数据为空: {ex}")
            raise ex

    def cases_delete(self, *, case: cases_schemas.CaseDatas):
        """
        删除用例，把数据从表中删除
        :param case:
        :return:
        """

        def select_(var1: typing.Any, var2: typing.Any):
            # 查询数据是否存在
            return self._session.execute(select(self._cases).where(var1 == var2)).scalars().first()

        try:
            # 如果数据不存在则抛出异常,存在则检查名称是否唯一
            datas = select_(self._cases.id, case.case_id)
            if not datas:
                raise Exception(f"数据不存在 ！")

            # 执行数据删除操作
            self._session.execute(
                delete(self._cases).where(self._cases.id == case.case_id)
            )

            # 提交并更新数据库
            self._session.commit()
            # self._session.refresh(datas_info)

            # 再次查询数据是否存在
            if select_(self._cases.id, case.case_id):
                raise Exception(f"{self._cases.id} 未删除成功 ！")

            return None

        except Exception as ex:
            do_logger.error(f"用例数据删除失败: {str(ex)}")
            raise ex

    def update_case_fields(self, *, case_id: int, **kwargs):
        """
        往Cases表中更新字段值
        :param case_id:
        :param kwargs:
        :return:
        """
        try:
            results = self._session.execute(
                update(self._cases).where(self._cases.id == case_id).values(**kwargs)
            )
            self._session.commit()
            self._session.refresh(results)
        except Exception as ex:
            raise ex

    def select_cases_get(self, *, case_id: typing.List):
        """
        查询测试用例执是否成功的字段
        :param case_id:
        :return:
        """
        results = self._session.execute(
            select(
                [self._cases.id, self._cases.is_success, self._cases.is_error, self._cases.is_fail]
            ).where(self._cases.id.in_(case_id))
        ).all()
        # datas = results.scalars().first()
        do_logger.info(results)
        return self._cases.is_json(results=results)

    def select_case_request(self, *, case_id):
        """
        查询测试用例请求数据
        :param case_id:
        :return:
        """
        try:
            results = self._session.execute(
                select(
                    [
                        self._cases.id, self._cases.name, self._cases.datas,
                        self._cases.expect, self._cases.comparison
                    ]
                ).where(self._cases.id == case_id, self._cases.is_active == 0)
            ).all()
            # do_logger.info(results)
            if results is None:
                raise
            return self._cases.is_json(results=results)
        except Exception as ex:
            do_logger.error(ex)
            raise ex
