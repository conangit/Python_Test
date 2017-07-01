#!/usr/bin/env python3
#-*-coding: utf-8 -*-

class Student(object):
    def __init__(self, name):
        self.name = name

# 实例属性
s = Student('Lihong')
s.age = 20

# 类属性
class A(object):
    name = 'class A'

print(A.name)

a = A()
print(a.name)
a.name = 'lihong'
print(a.name)       #实例属性优先级比类属性高
del a.name
print(a.name)
