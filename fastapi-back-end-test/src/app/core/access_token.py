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
from fastapi.exceptions import HTTPException
from src.conf.config import settings as st
from src.app.public.base_redis import redis_client


__all__ = [
    "AccessToken"
]


class AccessToken:

    @staticmethod
    def token_encrypt(*, data: dict, expires_delta: Union[timedelta, None] = None):
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

            # 对token进行加密
            results = jwt.encode(
                dict(data, **{"exp": expire}), st.SECRET, algorithm=st.ALGORITHM
            )
            return results
        except JWTError as exc:
            raise HTTPException(status_code=401, detail=exc)

    @staticmethod
    def token_decode(*, token: str):
        """
        解密Token
        @param  :
        @return  :
        """
        try:
            return jwt.decode(token, st.SECRET, algorithms=st.ALGORITHM)
        except JOSEError or JWTError:
            raise HTTPException(status_code=401, detail="凭证校验失败...")

    @staticmethod
    async def verify_token(token: str = Header(...)):
        """
        验证toekn是否有效
        @param  :
        @return  :
        """

        try:
            # Token解密
            handle_token = AccessToken.token_decode(token=token)
            username: str = handle_token.get("username")
            if not username:
                raise HTTPException(status_code=401, detail="凭证错误或验证失效...")
            # 从redis中获取Token再进行解密
            access_token = AccessToken.token_decode(
                token=await redis_client.get(f"access_token:{username}")
            )
            if (handle_token != access_token) or (not access_token) or (username != access_token["username"]):
                raise HTTPException(status_code=401, detail="凭证已失效, 请重新登录...")
        except Exception as exc:
            raise exc
