#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: code_response.py
@时间: 2023/06/02 08:14:42
@说明: 
"""

from fastapi.encoders import jsonable_encoder


__all__ = [
    "CodeResponse"
]


class CodeResponse:

    @staticmethod
    def succeed(status: int = 1, data: dict = None, err_msg=""):
        """
        接口成功需要返回的固定数据
        @param  :
        @return  :
        """
        return jsonable_encoder(
            dict(
                status=status,
                data=data if data else {},
                err_code=0,
                err_msg=err_msg
            )
        )

    @staticmethod
    def defeated(
        status: int = 0, data: dict = None, err_code: int = 1000, err_msg: str = "数据失败或被移除"
    ):
        """
        接口失败需要返回的固定数据
        @param  :
        @return  :
        """

        return jsonable_encoder(
            dict(
                status=status,
                data=data if data else {},
                err_code=err_code,
                err_msg=err_msg
            )
        )
