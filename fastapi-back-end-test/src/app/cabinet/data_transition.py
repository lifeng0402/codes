#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: data_transition.py
@时间: 2023/06/20 18:49:21
@说明: 
"""

import json
import datetime
import typing as ty


class Transition:

    @classmethod
    def json_translation_dict(cls, data: ty.Any):
        try:
            return data if isinstance(data, dict) else json.loads(data)
        except json.decoder.JSONDecodeError:
            return data

    @classmethod
    def json_translation_dict(cls, data: ty.Any):
        try:
            if not data:
                return data
            return json.dumps(data)
        except json.decoder.JSONDecodeError:
            return data
