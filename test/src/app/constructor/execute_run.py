#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/29 14:18
# @Author  : debugfeng
# @Site    : 
# @File    : execute_run.py
# @Software:

import ast
import json
import threading
import typing
from pydantic import HttpUrl
from fastapi import status
from sqlalchemy.orm import Session
from src.app.constructor import affirm
from src.app.crud.cases_crud import DatabasesCases
from src.app.crud.report_crud import DatabasesReport
from src.app.handler.client import HttpRequest
from src.app.enumeration.request_enum import BodyType


class ExecuteRun:
    def __init__(self, *, db: Session):
        self._http = HttpRequest()
        self._case = DatabasesCases(db=db)
        self._report = DatabasesReport(db=db)

    @staticmethod
    def _read_request(*, key: str, _list: list):
        """
        获取列表中数据
        :param key:
        :param datas_list:
        :return:
        """
        return tuple(i[key] for i in _list)[0]

    @staticmethod
    def _handle_report(*, key: str, results: typing.Any):
        """

        :param key:
        :param results:
        :return:
        """
        return len(tuple(su[key] for su in results if su is not None))

    def _handel_datas(self, datas: typing.Dict):

        if isinstance(datas, dict):
            pass
        if isinstance(datas, str):
            datas = json.loads(datas)

        data, request_data = datas, datas.get("datas")

        case_id = data.get("id")
        case_name = data.get("name")
        expect = data.get("expect")
        comparison = data.get("comparison")

        if not request_data:
            raise Exception("datas为空...")

        method = ExecuteRun._read_request(key="method", _list=request_data)
        url = ExecuteRun._read_request(key="url", _list=request_data)
        headers = ExecuteRun._read_request(key="headers", _list=request_data)
        body = ExecuteRun._read_request(key="body", _list=request_data)
        params = ExecuteRun._read_request(key="params", _list=request_data)
        cookies = ExecuteRun._read_request(key="cookies", _list=request_data)
        body_type = ExecuteRun._read_request(key="body_type", _list=request_data)

        response = self._http.request(
            method=method, url=url, headers=headers, body_type=body_type, body=body, params=params, cookies=cookies
        )

        try:
            # 如果是json就返回json格式，否则返回文本格式
            results = response.json() if body == BodyType.json else response.text.encode("utf-8")
            results_info = {"case_id": case_id, "actual": results}
            results_info["is_success"] = 1 if response.is_success else results_info["is_success"] = 2
            return results_info

        except Exception as ex:
            return ex

    def execute_cases(self, *, datas: typing.List):
        """
        执行测试用例
        :param datas:
        :return:
        """

        try:

            datas = self._case.select_case_request(case_id=datas)

            for case in datas:
                self._handel_datas(datas=case)

            total = len(datas)
            results = self._case.select_cases_get(case_id=datas)

            success = ExecuteRun._handle_report(key="is_success", results=results)
            error = ExecuteRun._handle_report(key="is_error", results=results)
            fail = ExecuteRun._handle_report(key="is_fail", results=results)
            percent = (success / (total - error)) * 100

            report_info = {
                "cases_id": list(datas), "total": total, "success": success, "error": error,
                "fail": fail, "percent": percent
            }
            self._report.insert_reports_info(report_datas=json.dumps(report_info))
            return report_info
        except Exception as ex:
            raise ex
