#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: base_redis.py
@时间: 2023/06/07 08:50:05
@说明: 
"""


import redis.asyncio as redis
from src.conf.config import settings

__all__ = [
    "redis_client"
]


redis_client = redis.Redis(
    host=settings.REDIS_SERVER,
    port=settings.REDIS_PORT, db=settings.REDIS_DB
)
