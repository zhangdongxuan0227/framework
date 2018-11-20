#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 15:19
# @Author  : zhangxingchen
# @Site    : zxcser@163.com
# @File    : overRIde.py
# @Software: PyCharm

class Bird(object):
    def jiji(self):
        print("make sound")


class chicken(Bird):
    def jiji(self):
        print("jjjj")


class frog(Bird):
    def jiji(self):
        super().jiji()
        print("呱呱呱")


bird = Bird()
bird.jiji()

ck = chicken()
ck.jiji()

qw = frog()
qw.jiji()

