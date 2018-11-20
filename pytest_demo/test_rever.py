#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/27 11:51
# @Author  : zhangxingchen
# @Site    : zxcser@163.com
# @File    : test_rever.py
# @Software: PyCharm
def reverse(string):
    return string[::-1]


def test_reverse():
    string = "good"
    assert reverse(string) == "doog"

    another_string = "itest"
    assert reverse(another_string) == "tseti"
