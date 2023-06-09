#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: dependencies.py
@时间: 2023/06/06 16:07:39
@说明: 
"""

from jose import (
    jwt,
    JWTError,
    JOSEError
)
from typing import Union
from datetime import (
    timedelta,
    datetime
)
from fastapi import Header
from src.conf.config import settings as st
from src.app.public.base_redis import redis_client


__all__ = [
    "AccessToken"
]


class AccessToken:

    @staticmethod
    def encryption_token(*, data: dict, expires_delta: Union[timedelta, None] = None):
        """
        Token加密
        @param  :
        @return  :
        """
        try:
            if expires_delta:
                expire = datetime.utcnow() + expires_delta
            else:
                expire = datetime.utcnow() + timedelta(days=50)

            results = jwt.encode(
                dict(data, **{"exp": expire}), st.SECRET, algorithm=st.ALGORITHM
            )
            return results
        except JWTError as exc:
            raise exc

    @staticmethod
    async def verify_token(token: str = Header(...)):
        """
        验证toekn是否有效
        @param  :
        @return  :
        """
        def token_decode(*, n_token: str):
            return jwt.decode(n_token, st.SECRET, algorithms=st.ALGORITHM)

        try:
            # Token解密
            results = token_decode(n_token=token)

            username: str = results.get("username")

            if not username:
                raise Exception("凭证错误或验证失效...")

            # 从redis中获取Token再进行解密
            access_token = token_decode(
                n_token=await redis_client.get(f"access_token:{username}")
            )

            if token != access_token or not access_token or username != access_token["username"]:
                raise Exception("凭证已失效, 请重新登录...")
        except Exception or JOSEError as exc:
            raise exc
