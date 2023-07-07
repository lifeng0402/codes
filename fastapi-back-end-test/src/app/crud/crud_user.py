#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: users.py
@时间: 2023/05/31 20:18:18
@说明:
"""

from sqlalchemy.orm import Session
from sqlalchemy import select
from src.app.schemas.user import (
    UseRregister, UsersLogin
)
from src.app.models.models_user import User
from src.app.core.hash_pwd import HashPassword
from src.app.core.base_redis import redis_client
from src.app.cabinet.transition import Transition
from src.app.cabinet.verification import VerificationData
from src.app.core.dependencies import DependenciesProject


__all__ = [
    "UsersCrud"
]


class UsersCrud:
    def __init__(self, *, session: Session) -> None:
        self.u = User
        self.db = session
        self.hash = HashPassword()

    def register(self, user: UseRregister):
        """
        注册接口数据和数据库交互
        @param  :
        @return  :
        """
        try:

            # 验证账号长度
            if not VerificationData.verification_lenth(var=user.username):
                raise Exception("账号长度为5-25个字符...")

            # 验证密码长度
            if not VerificationData.verification_lenth(var=user.password, max_len=25):
                raise Exception("密码长度为5-25个字符...")

            # 首先查询账号是否重复
            user_info = self.db.execute(
                select(self.u).where(self.u.username == user.username)
            )

            if user_info.scalars().first():
                raise Exception("账号已存在...")

            # 对密码进行加密, 再赋值给password变量
            password = self.hash.get_password_hash(password=user.password)

            # 获取到数据并赋值给users_info变量
            user_info = self.u(username=user.username, password=password)
            # 往数据库添加数据
            self.db.add(user_info)
            # 往数据库提交数据
            self.db.commit()
            # 刷新提交的数据
            self.db.refresh(user_info)

            result = self.db.execute(
                select(
                    self.u.id, self.u.username, self.u.created_time
                ).where(self.u.username == user.username)
            ).first()._asdict()

            return Transition.proof_timestamp(result)
        except Exception as exc:
            raise exc

    async def login(self, user: UsersLogin):
        """
        登录接口查询数据并返回
        @param  :
        @return  :
        """

        try:
            # 查询数据库的数据并转成字典格式
            user_info = self.db.execute(
                select(
                    self.u.id,
                    self.u.is_delete,
                    self.u.username,
                    self.u.created_time,
                    self.u.updated_time,
                    self.u.password
                ).where(
                    self.u.username == user.username
                )).first()._asdict()

            # 字典中取出密码
            hashed_password = user_info["password"]

            # 密码进行解密校验, 条件不满足则抛出异常
            if not self.hash.verify_password(user.password, hashed_password):
                raise Exception("账号或密码错误...")

            # 定义一个用于存储redis中的值并赋值给redis_key
            redis_key = f"access_token:{user_info['id']}"

            # 判断redis中是否存在token,不存在就写入
            if await redis_client.exists(redis_key):
                await redis_client.set(
                    redis_key,
                    DependenciesProject.jwt_encode(
                        # 创建一个只有用户ID的新字典, 用于生成token
                        data={k: v for k, v in user_info.items() if k == "id"},
                        expires_delta=7
                    )
                )

            # 从redis中读取token
            token = await redis_client.get(redis_key)

            # 判断token是否过期
            if not DependenciesProject.token_expiration(token=token):
                token = DependenciesProject.jwt_encode(
                    data={k: v for k, v in user_info.items() if k == "id"}
                )
                await redis_client.set(redis_key, token)

            # 生成一个清除密码的新字典，用于作返回值
            result = {k: v for k, v in user_info.items() if k != "password"}

            # 返回结果
            return Transition.proof_timestamp(dict(result, token=token))

        except Exception as exc:
            raise exc
