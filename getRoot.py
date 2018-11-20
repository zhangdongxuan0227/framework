#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 17:16
# @Author  : zhangxingchen
# @Site    : zxcser@163.com
# @File    : getRoot.py
# @Software: PyCharm

from logs import testf as t

path1 = t.getCurPath1()

path2 = t.getCurPath2()


import gc

print(gc.get_threshold())