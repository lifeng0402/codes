#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/21 18:34
# @Author  : debugfeng
# @Site    : 
# @File    : response_schemas.py
# @Software: PyCharm

from typing import Any
from pydantic import BaseModel


class SrcResponse(BaseModel):
    code: int
    msg: str
    data: Any
