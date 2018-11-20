#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 18:26
# @Author  : zhangxingchen
# @Site    : zxcser@163.com
# @File    : dubbo_API.py
# @Software: PyCharm
import json
import telnetlib


class Dubbo(telnetlib.Telnet):
    prompt = 'dubbo>'
    coding = 'utf-8'

    def __init__(self, host=None, port=0):
        super().__init__(host, port)
        self.write(b'\n')

    def command(self, flag, str_=""):
        data = self.read_until(flag.encode())
        self.write(str_.encode() + b"\n")
        return data

    def invoke(self, service_name, method_name):
        command_str = "invoke {0}.{1}()".format(
            service_name, method_name)
        self.command(Dubbo.prompt, command_str)
        data = self.command(Dubbo.prompt, "")
        data = json.loads(data.decode(Dubbo.coding, errors='ignore').split('\n')[0].strip())
        return data


if __name__ == '__main__':
    conn = Dubbo('serviceIp', 'port')
    result = conn.invoke(
        "serviceName",
        "serviceName.method"
    )
    print(result)
