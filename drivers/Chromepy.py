#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 16:12
# @Author  : zhangxingchen
# @Site    : zxcser@163.com
# @File    : Chromepy.py
# @Software: PyCharm

from selenium import  webdriver
import time
dr = webdriver.Chrome()

dr.maximize_window()
dr.implicitly_wait(8)

dr.get("https://www.baidu.com")

time.sleep(5)
dr.quit()