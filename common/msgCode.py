#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 17:31
# @Author  : zhangxingchen
# @Site    : zxcser@163.com
# @File    : msgCode.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup

import re

msg_url = "https://testlc.miuzone.com/lcApp/wap/msgCode"

'''
checktype:
1、注册 2、找回密码 3、设置提现密码 4、修改提现密码 7、设置或修改手势密码 9、金账户余额支付 提现
'''

checklist = ['1', '2', '3', '4', '7', '9']


def get_html(url, phone, code):
    querystring = {"phone": phone, "checkType": code, "phoneCode": "+"}
    headers = {
        'Cache-Control': "no-cache",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)  # 请求访问网站
    html = response.text  # 获取网页源码
    print(html)
    reg = '"values":"(.*?)"'
    pattern = re.compile(reg)
    url_list = pattern.findall(html)
    print(url_list)
    return url_list


print(get_html(msg_url, 18710000008, 1))




# for url in url_list:
#     filename = url[-20:]
#     response2 = requests.get(url, verify=False)
#     # 得到图片的二进制文件
#     print('正在%s保存二进制文件' % filename.encode('utf-8'))
#     with open('b_file/%s' % (filename), 'wb') as f:
#         f.write(response2.content)  # .content表示二进制文件，.text表示文本文件
print('爬取完成')
"""
==========================================================
"""
# print(response.text)
