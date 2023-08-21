#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: users.py
@时间: 2023/05/31 20:18:18
@说明:
"""

from sqlalchemy.orm import Session
from sqlalchemy import (
    select,
    delete,
    update
)
from src.app.schemas.user import (
    UseRregister,
    UsersLogin,
    UserChangePwd
)
from src.app.models.models_user import User
from src.app.core.hash_pwd import HashPassword
from src.app.core.base_redis import redis_client
from src.app.cabinet.transition import Transition
from src.app.cabinet.verification import VerificationData
from src.app.core.dependencies import DependenciesProject
from src.app.core.excpetions import DebugTestException


__all__ = [
    "UsersCrud"
]


class UsersCrud:
    def __init__(self, *, session: Session) -> None:
        self.u = User
        self.db = session
        self.hash = HashPassword()

    @staticmethod
    async def access_token(*, user_info: dict):
        try:
            # 定义一个用于存储redis中的值并赋值给redis_key
            redis_key: str = f"{user_info['id']}"
            # 加密token
            token = await DependenciesProject.verify_token(
                is_token=True, key_str=redis_key,
                encry_param={k: v for k, v in user_info.items() if k == "id"}
            )

            # 返回结果
            return dict(
                user=Transition.proof_dict(user_info, condition="password"), token=token
            )
        except Exception as exc:
            raise DebugTestException(message=exc)

    async def register(self, user: UseRregister):
        """
        新建账号存入到数据库

        :param user: 请求参数
        :type user: UseRregister
        :raises DebugTestException: 抛出异常
        :raises DebugTestException: 抛出异常
        :raises DebugTestException: 抛出异常
        :raises exc.message: 捕获异常错误
        :return: 
        :rtype: dict
        """
        try:
            # 验证账号长度
            if not VerificationData.verification_lenth(var=user.username):
                raise DebugTestException(message="账号长度为5-25个字符!")
            # 验证密码长度
            if not VerificationData.verification_lenth(var=user.password, max_len=25):
                raise DebugTestException(message="密码长度为5-25个字符!")

            # 查询账号是否重复SQL
            stmt = select(self.u.id, self.u.username, self.u.password).where(
                self.u.username == user.username)

            # 判断账号是否存在
            if self.db.execute(stmt).first():
                raise DebugTestException("账号已注册!")

            # 对密码进行加密, 再赋值给password变量
            password = self.hash.get_password_hash(password=user.password)
            # 获取到数据并赋值给users_info变量
            user_data = self.u(username=user.username, password=password)
            # 往数据库添加数据
            self.db.add(user_data)
            # 往数据库提交数据
            self.db.commit()
            # 刷新提交的数据
            self.db.refresh(user_data)

            # 再次执行SQL并转成字典类型
            user_info = self.db.execute(stmt).first()._asdict()

            return await UsersCrud.access_token(user_info=user_info)

        except Exception as exc:
            raise exc

    async def login(self, user: UsersLogin):
        """
        根据用户名称查询数据库数据
        数据库取出用户的密码和传入的密码进行比对

        :param user: 请求参数
        :type user: UsersLogin
        :raises DebugTestException: 抛出异常
        :raises exc.message: 捕获异常错误
        :return: 
        :rtype: dict
        """
        try:
            # 查询数据SQL
            stmt = select(self.u.id, self.u.username, self.u.password).where(
                self.u.username == user.username)

            # 执行SQL判断是否为真
            if not self.db.execute(stmt).first():
                raise DebugTestException(message="数据不存在或被删除!")

            # # 执行SQL并查询的数据转成字典
            user_info = self.db.execute(stmt).first()._asdict()

            # 字典中取出密码
            hashed_password = user_info["password"]

            # 密码进行解密校验, 条件不满足则抛出异常
            if not self.hash.verify_password(user.password, hashed_password):
                raise DebugTestException(message="账号或密码错误!")

            return await UsersCrud.access_token(user_info=user_info)

        except Exception as exc:
            raise exc

    async def change_password(self, user: UserChangePwd):
        """
        根据所传参数加密后存入数据库中

        :param user: 请求参数
        :type user: UserChangePwd
        :raises DebugTestException: 抛出异常
        :raises exc.message: 捕获异常错误
        :return: 
        :rtype: dict
        """
        try:
            # 对密码进行加密, 再从新赋值给password变量
            hash_password = self.hash.get_password_hash(password=user.password)
            # 更新用户密码
            self.db.execute(
                update(self.u).where(self.u.id == user.user_id).values(
                    password=hash_password)
            )
            self.db.commit()

            # 查询用户密码
            changed_password = self.db.execute(
                select(self.u.password).where(self.u.id == user.user_id)
            ).scalars().first()

            # 对比密码是否一致
            if not self.hash.verify_password(user.password, changed_password):
                raise DebugTestException(message="密码修改失败!")

            return dict(message="密码修改成功..")

        except DebugTestException as exc:
            raise exc.message

    async def logout(self, user_id: int):
        """
        根据用户ID删除Redis存储的Token

        :param user_id: 用户ID
        :type user_id: int
        :raises DebugTestException: 抛出异常
        :raises exc.message: 捕获异常错误
        :return: 
        :rtype: dict
        """
        try:
            redis_key = f"access_token:{user_id}"
            await redis_client.delete(redis_key)

            if await redis_client.exists(redis_key):
                raise DebugTestException(message="登出失败!")

            return dict(message="登出成功..")
        except DebugTestException as exc:
            raise exc.message

    async def sign_out(self, user_id: int):
        """
        根据用户ID从数据库中删除该用户
        再次查询是否删除成功

        :param user_id: 用户ID
        :type user_id: int
        :raises DebugTestException: 抛出异常
        :raises exc.message: 捕获异常错误
        :return: 
        :rtype: dict
        """
        try:
            # 执行删除数据动作
            self.db.execute(
                delete(self.u).where(self.u.id == user_id)
            )
            # 提交删除数据
            self.db.commit()

            # 根据用户ID查询数据
            user_info = self.db.execute(
                select(self.u).where(self.u.id == user_id)
            ).scalars().first()

            # 如果查询结果为真,就抛出异常
            if user_info:
                raise DebugTestException(message="注销失败!")

            # 返回删除用户成功的数据
            return dict(message="注销成功!")

        except DebugTestException as exc:
            raise exc.message
