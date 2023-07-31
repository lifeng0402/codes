#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: verification.py
@时间: 2023/06/02 16:23:10
@说明:
"""


import re
import json
from typing import AnyStr, Any
from verify_email import verify_email

__all__ = [
    "VerificationData"
]


class VerificationData:

    @staticmethod
    def verification(*, mobile: str):
        """
        验证手机号码是否符合规范
        @param  :
        @return  :
        """
        try:
            pattern = r'^1[3456789]\d{9}$'
            return re.match(pattern, mobile.strip()) is not None
        except Exception as exc:
            raise exc

    @staticmethod
    async def verification_email(*, email: AnyStr):
        """
        验证邮箱是否符合规范
        @param  :
        @return  :
        """
        try:
            # 用 asyncio.create_unverified_context() 函数创建一个未验证的上下文。
            # 这个上下文是非阻塞的，因此我们可以在主线程中继续执行其他操作，而 verify_email() 函数会在后台线程中运行。
            # 如果 verify_email() 函数验证邮件有效，则会在未验证的上下文中调用 print() 函数，否则会在主线程中抛出异常。
            async with verify_email.create_unverified_context() as ctx:
                result = await verify_email(email, ctx)
                return False if result.strip() else True
        except Exception as exc:
            raise exc

    @staticmethod
    def verification_lenth(*, var: AnyStr, max_len: int = 25, min_len: int = 5):
        """
        验证账号和密码的长度是否符合
        @param  :
        @return  :
        """
        try:
            return False if (len(var.strip()) > max_len) or (len(var.strip()) < min_len) else True
        except Exception as exc:
            raise exc

    @staticmethod
    def verification_json(var: Any):
        """
        验证是不是json数据

        :param var: 参数
        :type var: Any
        :return: 布尔型
        :rtype: bool
        """
        try:
            json.loads(var)
            return True
        except ValueError:
            return False
