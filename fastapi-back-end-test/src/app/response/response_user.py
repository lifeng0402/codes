#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: response_user.py
@时间: 2023/07/11 14:24:42
@说明: 
"""

from datetime import datetime
from pydantic import BaseModel


class ResponseUserModel(BaseModel):
    created_time: datetime
    updated_time: datetime
