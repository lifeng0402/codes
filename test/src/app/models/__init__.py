#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 09:39
# @Author  : debugfeng
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm

from sqlalchemy.orm import relationship
from src.app.public.databases import DATABASES
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# 定义一个ORM模型基类
BASE = declarative_base(DATABASES().ENGINE)
