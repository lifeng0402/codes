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
    JWTError
)
from typing import Union
from datetime import (
    timedelta,
    datetime
)
import typing as ty
from fastapi import Header
from fastapi.exceptions import HTTPException
from src.conf.config import settings as st
from src.app.core.base_redis import redis_client


__all__ = [
    "DependenciesProject"
]


class DependenciesProject:

    @staticmethod
    def jwt_encode(*, data: ty.Dict,  expires_delta: timedelta=10):
        """
        Token加密
        @param  :
        @return  :
        """
        try:

            expire_time = datetime.utcnow() + timedelta(days=expires_delta)

            # 对参数进行加密
            results = jwt.encode(
                dict(data, exp=expire_time), st.SECRET, algorithm=st.ALGORITHM
            )
            return results
        except JWTError as exc:
            raise exc

    @staticmethod
    def jwt_decode(*, token: str):
        """
        解密Token
        @param  :
        @return  :
        """
        try:
            return jwt.decode(token, st.SECRET, algorithms=st.ALGORITHM)
        except JWTError as exc:
            raise exc

    @staticmethod
    def token_expiration(*, token: str):
        """
        验证Token是否失效
        @param  :
        @return  :
        """
        try:
            result = DependenciesProject.jwt_decode(token=token)
            # 获取过期时间, 再将 Unix 时间戳转换为 datetime 对象
            expiration_datetime = datetime.fromtimestamp(result.get('exp'))
            # 获取当前时间
            current_datetime = datetime.now()
            
            # 判断是否过期, 条件为真返回False,否则返回True
            return False if expiration_datetime < current_datetime else True
        except Exception as exc:
            raise exc

    @staticmethod
    async def verify_token(token: str = Header(...)):
        """
        验证Toekn是否有效
        @param  :
        @return  :
        """

        try:
            # Token解密
            token_decode = DependenciesProject.jwt_decode(token=token)
            redis_key: str = f"access_token:{token_decode['id']}"

            if not await redis_client.exists(redis_key):
                raise HTTPException(status_code=401, detail="凭证错误或失效...")

            redis_token = await redis_client.get(redis_key)

            if not DependenciesProject.token_expiration(token=redis_token):
                raise HTTPException(status_code=401, detail="凭证错误或失效...111")

            return redis_token
        except Exception as exc:
            raise exc


if __name__ == "__main__":

    print(jwt.encode({"user_id": 222}, st.SECRET, algorithm=st.ALGORITHM))
