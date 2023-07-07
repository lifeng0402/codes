#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: hash_pwd.py
@时间: 2023/07/07 18:58:01
@说明: 
"""

from passlib.context import CryptContext

__all__ = [
    "HashPassword"
]


class HashPassword:
    def __init__(self) -> None:
        self.pwd_context = CryptContext(
            schemes=["bcrypt", "sha256_crypt"]
        )

    # 加密密码的函数
    def get_password_hash(self, password: str):
        return self.pwd_context.hash(password)

    # 验证密码的函数
    def verify_password(self, password: str, hashed_password: str):
        return self.pwd_context.verify(password, hashed_password)
