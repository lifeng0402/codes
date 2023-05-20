#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 16:31
# @Author  : debugfeng
# @Site    : 
# @File    : extract.py
# @Software: PyCharm

import re
import json
import typing
from jsonpath import jsonpath

__all__ = ["ExtractValue"]


class ExtractValue:

    @classmethod
    def json_extract(cls, response: typing.Any, expr: jsonpath):
        """
        json数据提取参数
        :param response:
        :param expr:
        :return:
        """
        try:
            if isinstance(response, dict):
                pass
            if isinstance(response, str):
                # 转成json字符串后再转成字典
                response = json.loads(json.dumps(response))
        except Exception as ex:
            raise Exception(f"错误信息：{ex}")
        else:
            results = jsonpath(response, expr=f"$.{expr}")
            return results if results else Exception("未提取到指定值，请检查 ！")

    @classmethod
    def regular_extract(cls, response: typing.Any, expr: str):
        """
        正则表达式提取参数
        :param response:
        :param expr:
        :return:
        """
        try:
            response = json.dumps(response)
        except json.JSONDecodeError as ex:
            raise Exception(f" json 数据解析失败：{ex}")
        else:
            results = re.search(pattern=expr, string=response)
            return re.findall(pattern=expr, string=response) if results else Exception("未提取到指定值，请检查 ！")


if __name__ == '__main__':
    datas = {
        "status": 1,
        "data": {
            "status": 1,
            "id": 897777,
            "token": "93afdf6c5b9214be269d1c37174be552",
            "user_type": 2,
            "company_id": 6923
        },
        "errMsg": "",
        "errCode": 0
    }
    # print(ExtractValue.extract(datas, expr="data.status"))
    print(jsonpath(datas, "$.data.token"))
    # print(json.loads(json.dumps(datas, indent=4)))
