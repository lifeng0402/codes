# -*- coding: utf-8 -*-
# @Time    : 2022/9/29 14:18
# @Author  : debugfeng
# @Site    : 
# @File    : execute.py
# @Software:

import ast
import json
import threading
import typing
from pydantic import HttpUrl
from fastapi import status
from sqlalchemy.orm import Session
from src.app.core import affirm
from src.app.crud.casesCrud import DatabasesCases
from src.app.crud.reportCrud import DatabasesReport
from src.app.utils.client import HttpRequest
from src.app.enumeration.requestEnum import BodyType


class ExecuteRun:
    def __init__(self, *, db: Session):
        self._http = HttpRequest()
        self._case = DatabasesCases(db=db)
        self._report = DatabasesReport(db=db)

    def execute_cases(self, case_id: int):

        if not case_id:
            raise

        request_info = self._case.select_case_request(case_id=case_id)

        case_id = request_info.get("id")
        case_name = request_info.get("name")
        datas = request_info.get("datas")
        expect = request_info.get("expect")
        comparison = request_info.get("comparison")

        if not datas:
            raise
        if isinstance(datas, dict):
            pass
        if isinstance(datas, str):
            datas = json.loads(datas)

        method = datas.get("method")
        url = datas.get("url")
        headers = datas.get("headers")
        body = datas.get("body")
        params = datas.get("params")
        cookies = datas.get("cookies")
        body_type = datas.get("body_type")

        try:
            # 开始请求接口
            results = self._http.request(
                method=method, url=url, headers=headers,
                body_type=body_type, body=body, params=params, cookies=cookies
            )
            # 如果是json就返回json格式，否则返回文本格式
            response = results.json() if body_type == BodyType.json else results.text.encode("utf-8")

            if expect and comparison:
                affirm.self_main(comparison=comparison, expect=expect, response=response)

            return response

        except Exception as ex:
            raise ex

    def execute_test_plan(self, *, case_id: typing.List):
        """
        执行测试计划
        :param case_id:
        :return:
        """

        try:
            total = 0
            for case in case_id:
                response = self.execute_cases(case_id=case)
                total += 1

            # total = len(datas)
            # results = self._case.select_cases_get(case_id=datas)
            # print(results)

            # success = ExecuteRun._handle_report(key="is_success", results=results)
            # error = ExecuteRun._handle_report(key="is_error", results=results)
            # fail = ExecuteRun._handle_report(key="is_fail", results=results)
            # percent = (success / (total - error)) * 100
            #
            # report_info = {
            #     "cases_id": list(datas), "total": total, "success": success, "error": error,
            #     "fail": fail, "percent": percent
            # }
            # self._report.insert_reports_info(report_datas=json.dumps(report_info))
            # return report_info
        except Exception as ex:
            raise ex
