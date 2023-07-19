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
from src.app.crud.crud_report_record import ReportRecord
from src.app.excpetions.debug_test import DebugTestException


class ExecuteCase:

    @staticmethod
    def generate_report(
        db: Session, *, total: int, total_succeed: int, total_defeated: int, total_error: int, success_rate: float
    ):
        try:
            report = ReportCrud(db)
            result = report.create_report(
                total=total, total_succeed=total_succeed,
                total_defeated=total_defeated, total_error=total_error, success_rate=success_rate
            )
            report_id = result["report_id"]

            return report.report_details(report_id=report_id)
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

            # 定义收集变量
            total, succeed, defeated, error = 0, 0, 0, 0

            # 循环列表获取请求参数
            for request_params in results["list"]:

                case_id = request_params["id"]
                copy_request_params = request_params.copy()

                del copy_request_params["id"]

                try:
                    # 发送请求
                    response = await RequestHttp.safe_request(**copy_request_params)
                    response_status = response["status"]

                    # 判断运行状态
                    if response_status:
                        succeed += 1
                    else:
                        defeated += 1

                except Exception as error_info:
                    total += 1
                    error += 1
                    print(error_info)
                    continue

                total += 1
            else:
                # 计算成功率,四舍五入保留2位小数
                success_rate = round((succeed / total) * 100, 2)
                # 写入数据库指定表中
                return ExecuteCase.generate_report(
                    db, total=total, total_succeed=succeed,
                    total_defeated=defeated, total_error=error, success_rate=success_rate
                )
        except DebugTestException as exc:
            print(exc)
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
