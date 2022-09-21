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


class TestResponse:

    @classmethod
    def encode_json(cls, data: Any):
        return jsonable_encoder(data, custom_encoder={datetime: lambda x: x.strftime("%Y-%m-%d %H:%M:%S")})

    @classmethod
    def successful(cls, code: int = 1, msg: str = "操作成功", data: Any = None):
        return TestResponse.encode_json(dict(code=code, msg=msg, data=data))

    @classmethod
    def defeated(cls, *, code: int = 0, msg: str = "操作失败", data: Any = None):
        return dict(code=code, msg=str(msg), data=data)
