#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/3 09:26
# @Author  : debugfeng
# @Site    : 
# @File    : users.py
# @Software: PyCharm

import flet
from flet import Page, Row, GridView, alignment, View
from flet import Text, TextField, ElevatedButton, Container


class Users:

    def __init__(self, page: Page):
        self._p = page
        self._p.title = "1024测试平台"
        self._p.horizontal_alignment = "center"
        self._p.vertical_alignment = "center"
        show = Text(value="1024测试平台", width=300, height=50)
        self._p.add(show)
        self.users()

    def register(self):
        self._p.views.append(
            View(
                "/register",
                [
                    TextField(label="username", width=300, height=50),
                    TextField(label="password", password=True, can_reveal_password=True, width=300, height=50),
                    TextField(label="手机号码", width=300, height=50),
                    TextField(label="邮箱地址", width=300, height=50),
                    TextField(label="姓名", width=300, height=50),
                    Row(
                        [
                            TextField(label="国籍", width=300, height=50),
                            TextField(label="省份", width=300, height=50),
                            TextField(label="城市", width=300, height=50)
                        ],
                        alignment="center"
                    ),
                    ElevatedButton("注册", on_click="/", width=300, height=50)
                ]
            )
        )
        self._p.update()

    def login(self):
        self._p.views.append(
            View(
                "/",
                [
                    TextField(label="username", width=300, height=50),
                    TextField(label="password", password=True, can_reveal_password=True, width=300, height=50),
                    TextField(label="mobile", width=300, height=50),
                    Row(
                        [
                            ElevatedButton("登录", on_click="", width=300, height=50),
                            ElevatedButton("注册", on_click=lambda _: self._p.go("/register"), width=300, height=50)

                        ],
                        alignment="center"
                    )
                ]
            )
        )
        self._p.update()

    def users(self):
        def view_pop(view):
            self._p.views.pop()
            top_view = self._p.views[-1]
            self._p.go(top_view.route)

        def route_change(route):
            self._p.views.clear()
            self.login()
            if self._p.route == "/register":
                self.register()
            if self._p.route == "/":
                self.login()

        self._p.on_route_change = route_change
        self._p.on_view_pop = view_pop
        self._p.go(self._p.route)


def main(page: Page):
    Users(page)


flet.app(target=main, view=flet.WEB_BROWSER)
