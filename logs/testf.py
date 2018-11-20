#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 10:06
# @Author  : zhangxingchen
# @Site    : zxcser@163.com
# @File    : testf.py
# @Software: PyCharm

# import timeit
#
# name = "zxc"
# age = "30"
# print(f"my name is {name},i am {age} years old")
#
# strings = ['foo', 'foobar', 'baz', 'qux', 'python', 'Guido Van Rossum']*100
#
#
# def test():
#     for i in strings:
#         if i == 'foo':
#             pass
#
#
# t = timeit.timeit(stmt=test, number=100000)
# print(t)



import os


def getCurPath1():
    cur_path = os.path.dirname(os.path.realpath(__file__))
    return cur_path


def getCurPath2():
    cur_path = os.getcwd()
    return cur_path


print(getCurPath1())

print(getCurPath2())