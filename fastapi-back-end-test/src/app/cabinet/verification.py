#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: verification.py
@时间: 2023/06/02 16:23:10
@说明:
"""


import re
from typing import AnyStr
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
        pattern = r'^1[3456789]\d{9}$'
        return re.match(pattern, mobile.strip()) is not None

    @staticmethod
    async def verification_email(*, email: AnyStr):
        """
        验证邮箱是否符合规范
        @param  :
        @return  :
        """
        # 用 asyncio.create_unverified_context() 函数创建一个未验证的上下文。
        # 这个上下文是非阻塞的，因此我们可以在主线程中继续执行其他操作，而 verify_email() 函数会在后台线程中运行。
        # 如果 verify_email() 函数验证邮件有效，则会在未验证的上下文中调用 print() 函数，否则会在主线程中抛出异常。
        async with verify_email.create_unverified_context() as ctx:
            result = await verify_email(email, ctx)
            return False if result.strip() else True

    @staticmethod
    def verification_lenth(*, var: AnyStr, max_len: int = 25, min_len: int = 5):
        """
        验证账号和密码的长度是否符合
        @param  :
        @return  :
        """
        return False if (len(var.strip()) > max_len) or (len(var.strip()) < min_len) else True


