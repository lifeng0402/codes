#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: code_enum.py
@时间: 2023/06/10 17:26:19
@说明: 
"""

from typing import (
    List, Dict, Text, Any, Union, Tuple
)
from enum import Enum, unique

__all__ = [
    "BodyType",
    "Environment",
    "Headers",
    "Cookies",
    "Validators",
    "Extractors",
    "ExpectedResult",
    "JsonData",
    "FormData",
    "Resp"
]


Resp = Union[Any, Dict]
JsonData = Dict[Text, Text]
FormData = Dict[Text, Text]
Headers = Dict[Text, Text]
Cookies = Dict[Text, Text]
Checkout = List[Dict[Text, Text]]
Extractors = Dict[Text, Text]
ExpectedResult = Dict[Text, Text]
TemplateData = Union[Any, Dict, Text, Tuple, List]


@unique
class BodyType(Enum):
    none: int = 0
    raw: int = 1
    graphql: int = 2
    form_data: int = 3
    binary: int = 4
    x_form_url: int = 5


@unique
class Environment(Enum):
    test: int = 0
    pre: int = 1
    pro: int = 2
