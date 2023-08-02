#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: cases_request.py
@时间: 2023/06/12 17:50:39
@说明:
"""

import typing as ty
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from src.app.core.http_request import RequestHttp
from src.app.cabinet.transition import Transition
from src.app.crud.crud_report import ReportCrud
from src.app.crud.crud_report_record import CrudReportRecord
from src.app.core.excpetions import DebugTestException
from src.app.core.validator_response import ResponseBase


class ExecuteCase:

    def __init__(self, session: Session) -> None:
        self._session = session
        self._report = ReportCrud(self._session)
        self._report_rd = CrudReportRecord(self._session)

    async def execute(self, results: ty.List[dict]):
        """
        批量执行读取用例并发送请求
        @param  :
        @return  :
        """

        try:
            # 生成一条报告数据
            generate_report = self._report.create_report()
            report_id = int(generate_report["report_id"])

            # 定义收集变量
            total, succeed, defeated, error = 0, 0, 0, 0

            # 循环列表获取请求参数
            for request_params in results["list"]:

                case_id = int(request_params["id"])
                extract = request_params["extract"]
                checkout = request_params["checkout"]

                # 复制一个字典用于发送请求
                copy_request_params = request_params.copy()

                # 去除要删除的key, 生成一个新的字典用于发送请求
                copy_request_params_handled = {
                    key: value for key, value in copy_request_params.items() if key not in [
                        "id", "extract", "checkout"
                    ]
                }

                try:
                    # 发送请求
                    response = await RequestHttp.safe_request(**copy_request_params_handled)
                    response_status = response["status"]

                    if checkout:
                        handel_response = ResponseBase(response=response)
                        assert_results = handel_response.validator(checkout)

                        # 获取断言后的状态
                        assert_status = assert_results["check_status"]

                    # 判断运行状态
                    if response_status or assert_status:
                        succeed += 1
                    else:
                        defeated += 1

                    # 数据插入数据库
                    self._report_rd.insert_record(
                        response=jsonable_encoder(response), report_id=report_id, case_id=case_id
                    )
                except DebugTestException as error_info:
                    error += 1
                    self._report_rd.insert_record(
                        response=f"{error_info.message}", report_id=report_id, case_id=case_id
                    )

                total += 1
            else:
                # 更新数据到指定测试报告
                self._report.update_report(
                    total=total, report_id=report_id,
                    total_succeed=succeed, total_defeated=defeated, total_error=error
                )

                # 获取报告的概况信息
                summarize = self._report.report_details(report_id=report_id)

                # 获取测试报告记录表中的记录详情
                running_results = CrudReportRecord(self._session).report_record_detalis(
                    report_id=report_id
                )

                # 返回数据
                return dict(summarize, details=running_results)

        except DebugTestException as exc:
            raise exc


if __name__ == "__main__":
    a = {
        'method': 'GET',
        'url': 'https://api-lms3.9first.com/manager/index/index/list',
        'body_type': '0',
        'body': None,
        'params': None,
        'headers': '{"token": "9d322f270932a2c3bcbbc532bbe899f8", "content_type": "application/json"}',
        'cookies': None,
        'content': None,
        'files': None,
        'expected_result': None
    }
