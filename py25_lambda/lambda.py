#!/usr/bin/env python3
#-*- coding: utf-8 -*-

L1 = [1, 2, 3, 4]
L2 = list(map(lambda i: i * i, L1))
print(L2)

f = lambda x: x + 5
print(f(5))


def build():
    return lambda x, y: x + y

f = build()
print(f)
print(f(4, 5))


'''
匿名函数是函数对象
匿名函数只有一个表达式
匿名参数也可以作为参数返回
Python对匿名函数支持有限
'''