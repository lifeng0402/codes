#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 15:28
# @Author  : debugfeng
# @Site    :
# @File    : access_token.py
# @Software: PyCharm

from jose import jwt
from jose import JWTError
from fastapi import Header
from typing import Optional
from config import Confing
from passlib.context import CryptContext
from datetime import datetime, timedelta
from src.app.public.operationalRedis import redispy
from jose.exceptions import ExpiredSignatureError


__all__ = ["AccessToken"]


class AccessToken:
    _KEY, _ALGORITHM, _TOKEN_EXPIRE_DAYS = Confing.ACCESS_TOKEN_EXPIRE
    _ENCRYPTION_PWD = CryptContext(schemes=Confing.TOKEN_ENCRYPTION)

    @classmethod
    def generate_access_token(cls, data: dict, expiration: Optional[timedelta] = None):
        """
        生成token并加密
        :param data:
        :param expiration:
        :return:
        """
        to_encode = data.copy()
        expire = datetime.utcnow() + expiration if expiration else datetime.utcnow() + \
            timedelta(days=3)
        to_encode.update({"exp": expire})
        to_encode_jwt = jwt.encode(
            to_encode, key=cls._KEY, algorithm=cls._ALGORITHM
        )
        return to_encode_jwt, expire

    @classmethod
    def verify_token(cls, token: str = Header(...)):
        """
        获取用户并解密token
        :param token:
        :return:
        """

        try:
            #   解析token值
            payload = jwt.decode(
                token, key=cls._KEY, algorithms=cls._ALGORITHM
            )
            username: str = payload["username"]
            exception_info = Exception(" 凭证错误或失效啦...... ")
            #   判断用户是不是空值
            if username is None:
                raise exception_info
            #  redis读取token值
            redis_token = redispy.get_value(username, is_data=True)
            #   如不满足条件则抛出错误
            if not username and not redis_token and redis_token != token:
                raise exception_info
        except ExpiredSignatureError:
            raise Exception(" 登录凭证失效，请重新登录 ！")
        except Exception or JWTError:
            raise Exception("登录状态校验失败, 请重新登录 ！")

    @classmethod
    def encryption_password(cls, *, pwd: str):
        """
        接口到密码后进行加密处理
        :param pwd:
        :return:
        """
        password = cls._ENCRYPTION_PWD.hash(pwd)
        return password

    @classmethod
    def decode_password(cls, *, pwd: str, hashed_password: str):
        """
        接收到密码后进行解密
        :param pwd:
        :param hashed_password:
        :return:
        """

        password = cls._ENCRYPTION_PWD.verify(pwd, hashed_password)
        return password


if __name__ == '__main__':
    print(AccessToken.decode_password(
        pwd="1234567",
        hashed_password='$5$rounds=535000$A2.mDJP4Hk3U63p2$pfCvAUthxtyayocsQD8whBo/mizLVrEcFDnY3Ia7kN/')
    )
