#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/28 15:32
# @Author  : zhangxingchen
# @Site    : zxcser@163.com
# @File    : myRedis.py
# @Software: PyCharm
import redis


class myRedis(object):
    def __init__(self, ip, pwd, port=6379, db=0):
        try:
            self.conn = redis.Redis(host=ip, password=pwd, port=port, db=db)  # 连接redis
            print("连接成功")
        except Exception as e:
            print("redis 连接失败,错误信息为%s" % e)

    def str_get(self, k):
        res = self.conn.get(k)  # 会从服务器传对应的值过来，性能慢
        if res:
            return res.decode()  # 从redis里面拿到的是bytes类型的数据，转换成unicode

    def str_set(self, k, v, time=None):  # time默认失效时间
        self.conn.set(k, v, time)

    def delete(self, k):
        tag = self.conn.exists(k)
        # 判断这个key是否存在,相对于get到这个key他只是传回一个存在会不会存在的信息，
        # 而不用将整个k值传过来（如果k里面存的东西比较多，那么传输很耗时）
        if tag:
            self.conn.delete(k)
        else:
            print('这个key不存在')

    def hash_get(self, name, k):  # 哈希类型存储的是多层字典（嵌套字典）
        res = self.conn.hget(name, k)
        if res:
            return res.decode()  # 因为get不到值得话也不会报错所以需要判断一下

    def hash_set(self, name, k, v):  # 哈希类型的是多层
        self.conn.hset(name, k, v)  # set也不会报错

    def hash_getall(self, name):
        res = self.conn.hgetall(name)  # 得到的是字典类型的，里面的k,v都是bytes类型的
        data = {}
        if res:
            for k, v in res.items():  # 循环取出字典里面的k,v，在进行decode
                k = k.decode()
                v = v.decode()
                data[k] = v
        return data

    def hash_del(self, name, k):
        res = self.conn.hdel(name, k)
        if res:
            print('删除成功')
            return 1
        else:
            print('删除失败，该key不存在')
            return 0

    @property  # 属性方法，
    # 使用的时候和变量一个用法就好比实例，A=MyRedis(), A.clean_redis使用，
    # 如果不加这个@property,使用时A=MyRedis(), A.clean_redis()   后面需要加这个函数的括号
    def clean_redis(self):
        self.conn.flushdb()  # 清空 redis
        print('清空redis成功！')
        return 0


if __name__ == '__main__':
    a = myRedis('10.105.10.113', 'testredis')
    keys =a.conn.keys()
    print(type(keys))
    #print(keys)
    new_list=[]

    for i in keys:
        str_keys = i.decode()
        new_list.append(str_keys)

    print(new_list)



