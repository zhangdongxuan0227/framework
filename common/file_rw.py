#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 17:33
# @Author  : zhangxingchen
# @Site    : zxcser@163.com
# @File    : file_rw.py
# @Software: PyCharm

class Writefile(object):
    file = 'chars.txt'

    def w_file(self, data):
        try:
            with open(self.file, 'wt') as wf:
                wf.writelines(data)
        except Exception as e:
            print(e)

    def r_file(self):
        try:
            with open(self.file, 'r') as rf:
                data=rf.readlines()
                return [each.strip() for each in data]

        except Exception as e:
            print(e)
