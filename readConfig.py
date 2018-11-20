#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/20 21:03
# @Author  : zhangxingchen
# @Site    : zxcser@163.com
# @File    : readConfig.py
# @Software: PyCharm


import configparser
import os

root = os.getcwd()
config_file = "config.ini"
fp = os.path.join(root, config_file)
print(fp)
config = configparser.ConfigParser()
config.read(fp, encoding='utf8')
print(config.sections())

print(config.options('mysql'))