#!/usr/bin/env python3
# _*_coding: utf-8 _*_

abs(-10)
abs

# 函数参数可以为另一个函数
def add(x, y, f):
    return f(x) + f(y)

x = -5
y = 6
f = abs
s = add(x, y, f)
print(s)

