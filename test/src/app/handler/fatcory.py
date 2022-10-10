#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/21 17:28
# @Author  : debugfeng
# @Site    : 
# @File    : fatcory.py
# @Software: PyCharm

from typing import Any
from datetime import datetime
from fastapi.encoders import jsonable_encoder

__all__ = ["TestResponse"]


class TestResponse:

    @classmethod
    def _encode_json(cls, data: Any):
        """
        接收的数据处理成json返回
        :param data:
        :return:
        """
        return jsonable_encoder(
            data, custom_encoder={datetime: lambda x: x.strftime("%Y-%m-%d %H:%M:%S")}
        )

    @classmethod
    def successful(cls, status: int = 1, msg: str = "操作成功", data: Any = None, response: Any = None):
        """
        接口请求成功的返回方法
        :param status:
        :param msg:
        :param data:
        :param response:
        :return:
        """
        if response:
            return cls._encode_json(dict(response))
        return cls._encode_json(dict(code=status, msg=msg, data={} if data is None else data))

    @classmethod
    def defeated(cls, *, status: int = 0, msg: str = "操作失败", data: Any = None, response: Any = None):
        """
        接口请求失败的返回方法
        :param status:
        :param msg:
        :param data:
        :param response:
        :return:
        """
        if response:
            return cls._encode_json(dict(response))
        return dict(code=status, msg=str(msg), data={} if data is None else data)
