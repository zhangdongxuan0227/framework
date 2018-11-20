#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 16:18
# @Author  : zhangxingchen
# @Site    : zxcser@163.com
# @File    : conn_miuzone.py
# @Software: PyCharm


import pymysql
import configparser

config = {
    "host": '10.105.10.79',
    "port": 3306,
    "user": 'test_ydxsb',
    "password": 'test_ydxsb',
    "db": 'test_ydxsb',
    "charset": 'utf8'
}

sql = "SELECT PRODUCT_NO FROM dwf_product WHERE JF_PRODUCT_NO='MIUZONE_006'"

listdata = []
# 创建连接 事务
conn = pymysql.connect(**config)
# 创建游标
cur = conn.cursor()

try:
    result = cur.execute(sql)

    data = cur.fetchall()

    conn.commit()
except:
    conn.rollback()

for i in data:
    print(i)
    listdata.append(i)
# 关闭游标
cur.close()
# 关闭数据库
conn.close()

print(result)
print(data)
print(listdata)