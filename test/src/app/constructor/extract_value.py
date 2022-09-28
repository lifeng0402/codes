#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 16:31
# @Author  : debugfeng
# @Site    : 
# @File    : extract_value.py
# @Software: PyCharm

import json
import typing
from jsonpath import jsonpath


class ExtractValue:
    pass

    @classmethod
    def extract(cls, response: typing.Any, expr):
        if isinstance(response, dict):
            response = json.loads(json.dumps(response))
            return response
            # return jsonpath(response, expr=f"$.{expr}")


if __name__ == '__main__':
    datas = {
    "code": 1,
    "msg": "接口请求数据添加成功 ！",
    "data": {
        "method": "post",
        "headers": {"Content-Type": "application/json; charset=UTF-8"},
        "title": "登录接口4444",
        "params": "None",
        "cookies": "None",
        "created_time": "2022-09-28 14:30:09",
        "url": "https://api-lms3.9first.com/user/auth",
        "id": 6,
        "body_type": 1,
        "body": {'user_name': 'account01', 'password': 'account01', 'scenario': 'web', 'day': 1},
        "is_active": "true",
        "updated_time": "2022-09-28 14:30:09"
    }
}
    # print(ExtractValue.extract(datas, expr="data.headers.Content-Type"))
    print(json.dumps(datas, indent=2))
    # print(json.loads(json.dumps(datas, indent=4)))
