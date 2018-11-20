#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 11:11
# @Author  : zhangxingchen
# @Site    : zxcser@163.com
# @File    : daily_pra.py
# @Software: PyCharm


# i = 10
# if i > 4:
#     print("ok")
#     if i > 6:
#         print("ojbk")


class Vow(object):
    def __init__(self, text):
        self.text = text

    def __enter__(self):
        self.text = "i say" + self.text
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.text = self.text + "&&&&"


with Vow("hello") as myvow:
    print(myvow.text)


print(myvow.text)


# 序列化 和 反序列化
import pickle
import time
print(time.time())