#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: dantic.py
@时间: 2023/05/31 14:11:18
@说明: 
"""

from pydantic import AnyUrl


__all__ = [
    "DatabasesDsn"
]


class DatabasesDsn(AnyUrl):
    allowed_schemes = {
        'mysql+pymysql',
        'postgresql',
        'postgresql+asyncpg',
        'postgresql+pg8000',
        'postgresql+psycopg',
        'postgresql+psycopg2',
        'postgresql+psycopg2cffi',
        'postgresql+py-postgresql',
        'postgresql+pygresql',
    }