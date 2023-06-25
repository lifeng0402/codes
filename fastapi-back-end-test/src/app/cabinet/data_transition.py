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


class Transition:

    @classmethod
    def string_json(cls):
          pass
    
    
    
a = {
    "status": 1,
    "data": {
        "method": "GET",
        "body_type": "0",
        "content": None,
        "params": None,
        "cookies": None,
        "timeout": None,
        "plan_id": None,
        "updated_time": "2023-06-25T11:44:22",
        "url": "https://api-lms3.9first.com/manager/index/index/list",
        "body": None,
        "id": 16,
        "files": None,
        "headers": "{\"token\": \"9d322f270932a2c3bcbbc532bbe899f8\", \"content_type\": \"application/json\"}",
        "expected_result": None,
        "created_time": "2023-06-25T11:44:22"
    },
    "err_code": 0,
    "err_msg": "添加成功"
}

for k in a["data"]:
      print(k)
      # if r"{" in v and r"}" in v:
      #       print(json.loads(k=v))