#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/16 09:39
# @Author  : debugfeng
# @Site    : 
# @File    : main.py
# @Software: PyCharm

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    pass
