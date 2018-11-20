#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/27 17:01
# @Author  : zhangxingchen
# @Site    : zxcser@163.com
# @File    : performance_test1.py
# @Software: PyCharm

from locust import HttpLocust, TaskSet, task


class Userbehave(TaskSet):
    @task
    def baidu(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    task_set = Userbehave
    min_wait = 1000
    max_wait = 2000
    host = "https://www.baidu.com"
