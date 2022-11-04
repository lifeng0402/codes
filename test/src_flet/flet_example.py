#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/20 19:36
# @Author  : debugfeng
# @Site    : 
# @File    : flet_example.py
# @Software: PyCharm

import flet
from flet import IconButton, Page, Row, TextField, icons, Text


def main(page: Page):
    page.title = "Flet counter example"
    page.vertical_alignment = "center"

    # txt_number = TextField(value="0", text_align="right", width=100)

    # def minus_click(e):
    #     txt_number.value = int(txt_number.value) - 1
    #     page.update()
    #
    # def plus_click(e):
    #     txt_number.value = int(txt_number.value) + 1
    #     page.update()

    # page.add(
    #     Row(
    #         [
    #             IconButton(icons.REMOVE, on_click=minus_click),
    #             txt_number,
    #             IconButton(icons.ADD, on_click=plus_click),
    #         ],
    #         alignment="center",
    #     )
    # )
    # t = Text(value="Hello World", color="green")
    # page.controls.append(t)
    # page.update()
    page.add(
        Row(controls=[
            Text("A"),
            Text("B"),
            Text("C")
        ])
    )


flet.app(target=main, port=8888, view=flet.WEB_BROWSER)
