#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/28 11:11
# @Author  : zhangxingchen
# @Site    : zxcser@163.com
# @File    : practice1.py
# @Software: PyCharm

fangjia = 500000.0
year = 0
lixi = [0.01, 0.02, 0.03, 0.04]

repay = 30000.0

while fangjia > 0:
    year += 1
    print("第", year, "年要还钱")

    if year <= 4:
        irr = lixi[year - 1]
    else:
        irr = 0.05
    fangjia = fangjia + fangjia * irr - repay


def pack_position(*args):
    print(type(args))
    print(args)


pack_position(1, 3, 4)
pack_position(666, 232, 3223)


def pack_position1(**args):
    print(type(args))
    print(args)


con = {"a": '1', 'b': '2'}
# 解包裹
pack_position1(**con)


def pack_mix(*args, **args1):
    print(args, end='')
    print(args1)


pack_mix(1, 2, 3, a=1, b=2)

import time

print(time.__name__)

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write("nihaoshuai")

print(f.closed)