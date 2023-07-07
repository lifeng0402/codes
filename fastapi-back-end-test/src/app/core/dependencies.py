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
    def jwt_encode(*, data: ty.Dict, expires: Union[timedelta, None] = None):
        """
        Token加密
        @param  :
        @return  :
        """
        try:
            utcnow = datetime.utcnow()
            expire_time = utcnow + \
                expires if expires else utcnow + timedelta(days=50)
            print(expire_time)
            # 对参数进行加密
            results = jwt.encode(
                dict(data, exp=expire_time), st.SECRET, algorithm=st.ALGORITHM
            )
            return results
        except JWTError as exc:
            raise HTTPException(status_code=401, detail=exc)

    @staticmethod
    def jwt_decode(*, token: str):
        """
        解密Token
        @param  :
        @return  :
        """
        try:
            result = jwt.decode(token, st.SECRET, algorithms=st.ALGORITHM)

            # 获取过期时间, 再将 Unix 时间戳转换为 datetime 对象
            expiration_datetime = datetime.fromtimestamp(result.get('exp'))
            # 获取当前时间
            current_datetime = datetime.now()

            # 判断是否过期, 条件为真返回False,否则返回True
            return False if expiration_datetime > current_datetime else True

        except JWTError as exc:
            raise HTTPException(status_code=401, detail=exc)

    @staticmethod
    async def verify_token(token: str = Header(...)):
        """
        验证toekn是否有效
        @param  :
        @return  :
        """

        try:
            # Token解密
            decode = DependenciesProject.jwt_decode(token=token)
            user_id: str = decode.get("user_id")
            if not user_id:
                raise HTTPException(status_code=401, detail="凭证错误或失效...")

            # 从redis中获取Token再进行解密
            access_token = DependenciesProject.jwt_decode(
                token=await redis_client.get(f"token:{user_id}")
            )

            # if (handle_token != access_token) or (not access_token) or (username != access_token["username"]):
            #     raise HTTPException(status_code=401, detail="凭证已失效, 请重新登录...")
        except Exception as exc:
            raise exc


if __name__ == "__main__":

    print(jwt.encode({"user_id": 222}, st.SECRET, algorithm=st.ALGORITHM))
