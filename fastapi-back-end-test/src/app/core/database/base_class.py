#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@作者: debugfeng
@文件: base_class.py
@时间: 2023/05/31 10:14:07
@说明: 
"""


from sqlalchemy.ext.declarative import (
    declared_attr, as_declarative
)


# as_declarative将一个类或模型转换为声明式模式。
# 这个函数的作用是将类或模型中的所有属性转换为类属性或实例属性，同时将所有的方法转换为非懒加载方法。
# 转换完成后，该类或模型就可以像声明式的对象一样使用了。
@as_declarative()
class Base:
    __name__: str

    # 函数可以用来获取模型中声明的属性。它返回一个字典，其中键是属性名称，值是属性对应的类属性或实例属性。
    # 这个函数通常用在ORM模型中，可以用来获取模型中被声明的属性，并将其添加到调用函数的参数中。
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
