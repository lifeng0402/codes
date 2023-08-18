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
    ExpiredSignatureError
)
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
    def jwt_encode(*, data: ty.Dict,  expires_delta: timedelta = 10):
        """
        Token加密
        @param  :
        @return  :
        """
        try:
            expire_time = datetime.utcnow() + timedelta(days=expires_delta)
            # 对参数进行加密
            results = jwt.encode(
                dict(data, exp=expire_time),
                st.SECRET, algorithm=st.ALGORITHM
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
        except ExpiredSignatureError:
            # Redis读取的token是否过期
            return False
        except Exception as exc:
            raise exc

    @staticmethod
    async def verify_token(*, key_str: str, encry_param: dict = None, is_token: bool = False):
        """
        验证token是否为空、不存在、失效等
        @param  :
        @return  :
        """

        try:
            # redis_key值
            redis_key = f"access_token:{key_str}"
            # 从redis中读取token用于判断
            result_token = await redis_client.get(redis_key)
            print(222, DependenciesProject.token_expiration(token=result_token))
            # 判断redis中是否存在token,token是否过期, token是不是None,如条件满足就写入
            if not await redis_client.exists(redis_key) or not result_token or not DependenciesProject.token_expiration(token=result_token):
                if is_token:
                    if not encry_param:
                        raise Exception("encry_param字段不能为空...")

                    # 把生成的token写入到redis中存储
                    await redis_client.set(
                        redis_key, DependenciesProject.jwt_encode(
                            data=encry_param)
                    )
                    # 从redis中读取token并复制给token变量
                    result_token = await redis_client.get(redis_key)
                else:
                    raise HTTPException(
                        status_code=401,
                        detail=dict(status=401, message="凭证错误或失效...")
                    )
            return result_token.decode("utf-8")

        except Exception as exc:
            raise exc

    @staticmethod
    async def dependence_token(token: str = Header(...)):
        """
        验证Toekn是否有效
        @param  :
        @return  :
        """

        try:
            # Token解密
            token_decode = DependenciesProject.jwt_decode(token=token)
            # 读取value的key
            redis_key: str = f"{token_decode['id']}"
            redis_token = await DependenciesProject.verify_token(key_str=redis_key)

            # 验证所传token和登录存储在redis中的token是否一致。
            if DependenciesProject.jwt_decode(token=redis_token) != token_decode:
                raise HTTPException(
                    status_code=401,
                    detail=dict(status=401, message="凭证错误或失效...")
                )
            return redis_token
        except Exception as exc:
            raise exc


if __name__ == "__main__":

    print(DependenciesProject.token_expiration(
        token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwiZXhwIjoxNjkwNzA4ODU4fQ.8nsSsE6gwjC1J9XGF_zv2zbqsj6oMXkwE6dlozXiiWE"
    ))
