#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 16:09
# @Author  : zhangxingchen
# @Site    : zxcser@163.com
# @File    : RandomChar.py
# @Software: PyCharm

import itertools


def create_chars():
    chars = [chr(c) for c in range(97, 123)]
    char_tuple = itertools.permutations(chars, 4)
    char_data = ['www.' + ''.join(each) + '.com' + '\n' for each in char_tuple]
    return char_data


if __name__ == '__main__':
    print(create_chars())
