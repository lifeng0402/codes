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

    @staticmethod
    def get_report_record_data(db: Session, *, report_id: int):
        """
        根据report_id获取运行用例的具体情况
        @param  :
        @return  :
        """
        try:
            # 获取详情数据并返回
            return CrudReportRecord(db).report_record_detalis(report_id=report_id)
        except DebugTestException as exc:
            raise exc

    @staticmethod
    def insert_report_record_data(
        db: Session, *, report_id: int, case_id: int, response: ty.Union[dict, str, None]
    ):
        """
        往测试报告记录表中插入数据
        根据report_id去查询测试报告记录表,然后返回数据

        @param  :
        @return  :
        """
        try:
            # 生成数据
            CrudReportRecord(db).insert_record(
                response=response, report_id=report_id, case_id=case_id
            )
            return True
        except DebugTestException as exc:
            raise exc

    @staticmethod
    def update_report_data(
        db: Session, *, report_id: int, total: int, total_succeed: int, total_defeated: int, total_error: int
    ):
        """
        往测试报告表中更新指定report_id的数据
        根据report_id去查询测试报告概况详情数据,然后返回数据
        @param  :
        @return  :
        """
        try:
            report = ReportCrud(db)
            # 更新指定测试报告的概况数据
            result = report.update_report(
                total=total, report_id=report_id,
                total_succeed=total_succeed, total_defeated=total_defeated, total_error=total_error
            )
            # 提取report_id
            report_id = result["report_id"]

            # 获取详情数据并返回
            return report.report_details(report_id=report_id)
        except DebugTestException as exc:
            raise exc

    @staticmethod
    def generate_report(db: Session):
        """
        往测试报告表中创建一条数据
        @param  :
        @return  :
        """
        try:
            # 生成数据操作
            results = ReportCrud(db).create_report()
            return int(results["report_id"])
        except DebugTestException as exc:
            raise exc

    @staticmethod
    async def execute(results: ty.List[dict], db: Session):
        """
        批量执行读取用例并发送请求
        @param  :
        @return  :
        """

        try:
            # 生成一条报告数据
            report_id = ExecuteCase.generate_report(db)

            # 定义收集变量
            total, succeed, defeated, error = 0, 0, 0, 0

            # 循环列表获取请求参数
            for request_params in results["list"]:

                case_id = int(request_params["id"])
                extract = request_params["extract"]
                checkout = request_params["checkout"]

                # 复制一个字典用于发送请求
                copy_request_params = request_params.copy()
                # 提取出要删除的key
                keys_to_delete = ["id", "extract", "checkout"]
                # 去除要删除的key, 生成一个新的字典用于发送请求
                copy_request_params_handled = {
                    key: value for key, value in copy_request_params.items() if key not in keys_to_delete
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

                    # 数据写入数据库
                    ExecuteCase.insert_report_record_data(
                        db, case_id=case_id,
                        report_id=report_id,
                        response=jsonable_encoder(response)
                    )
                except DebugTestException as error_info:
                    error += 1
                    ExecuteCase.insert_report_record_data(
                        db, case_id=case_id,
                        report_id=report_id,
                        response=f"{error_info.message}"
                    )

                total += 1
            else:
                # 更新数据到指定测试报告
                summarize = ExecuteCase.update_report_data(
                    db, report_id=report_id, total=total,
                    total_succeed=succeed, total_defeated=defeated, total_error=error
                )
                # 获取测试报告记录表中的记录详情
                running_results = ExecuteCase.get_report_record_data(
                    db, report_id=report_id
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
