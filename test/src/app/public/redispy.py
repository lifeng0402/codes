# -*- encoding: utf-8 -*-
"""
@__Author__: lifeng
@__Software__: PyCharm
@__File__: redispy.py
@__Date__: 2022/5/8 11:28
"""

import redis
from src.app import setting as st

__all__ = ["redispy"]


class _Redispy:
    def __init__(self):
        _connect_ip = st.REDIS_DATABASES["PRO"] if st.ENVIRONMENT else st.REDIS_DATABASES["TEST"]
        self._connect = redis.Redis(host=_connect_ip, port=6379, db=1)

    def set_value(self, name: str, value: str, is_data: bool = False):
        """
        往redis写入数据
        :param name:
        :param value:
        :param is_data:
        :return:
        """
        if is_data:
            name = f"token:{name}"
        self._connect.set(name, value)

    def get_value(self, name: str, is_data: bool = False):
        """
        从redis获取value
        :param name:
        :param is_data:
        :return:
        """
        if is_data:
            name = f"token:{name}"

        return self._connect.get(name).decode('utf-8')

    def delete_value(self, name: str, is_data: bool = False):
        if is_data:
            name = f"token:{name}"
        return self._connect.delete(name)

    def get_exists(self, name, is_data: bool = False):
        """
        判断redis中的key是否存在
        :param name:
        :param is_data:
        :return:
        """
        if is_data:
            name = f"token:{name}"
        return self._connect.exists(name)

    def __del__(self):
        self._connect.close()


redispy = _Redispy()
