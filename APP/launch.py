#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 18:27
# @Author  : zhangxingchen
# @Site    : zxcser@163.com
# @File    : launch.py
# @Software: PyCharm


from appium import webdriver

desired_caps = {

                'platformName': 'Android',

                'deviceName': '49aad0089904',

                'platformVersion': '7.0',

                # apk包名

                'appPackage': 'com.chainfin.meter',

                # apk的launcherActivity

                'appActivity': 'com.chainfin.meter.AppStart'

                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
