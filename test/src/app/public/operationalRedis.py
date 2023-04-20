# -*- encoding: utf-8 -*-
"""
@__Author__: lifeng
@__Software__: PyCharm
@__File__: redispy.py
@__Date__: 2022/5/8 11:28
"""

import redis
from redis import Redis
from src.config import Confing

__all__ = ["redispy"]


class _OperRedis:
    def __init__(self):
        self._connect = Redis(**Confing.REDIS_DATABASE_URI)

    def set_value(self, name: str, value: str, is_data: bool = False):
        """
        往redis写入数据
        :param name:
        :param value:
        :param is_data:
        :return:
        """
        try:
            if is_data:
                name = f"token:{name}"
            self._connect.set(name, value)
        finally:
            self._connect.close()

    def get_value(self, name: str, is_data: bool = False):
        """
        从redis获取value
        :param name:
        :param is_data:
        :return:
        """
        try:
            if is_data:
                name = f"token:{name}"
            return self._connect.get(name).decode('utf-8')
        finally:
            self._connect.close()

    def delete_value(self, name: str, is_data: bool = False):
        try:
            if is_data:
                name = f"token:{name}"
            return self._connect.delete(name)
        finally:
            self._connect.close()

    def get_exists(self, name, is_data: bool = False):
        """
        判断redis中的key是否存在
        :param name:
        :param is_data:
        :return:
        """
        try:
            if is_data:
                name = f"token:{name}"
            return self._connect.exists(name)
        finally:
            self._connect.close()



redispy = _OperRedis()

