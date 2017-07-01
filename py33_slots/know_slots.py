#!/usr/bin/env python3
# -*-coding: utf-8 -*-

from types import MethodType

class Student(object):
    pass

# 实例绑定属性
s = Student()
s.name = 'lihong'
print(s.name)

# 实例绑定方法
def set_age(self, age):
    self.age = age

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

'''
s1 = Student()
s1.set_age(20)    #动态绑定方法只对该实例有用
'''

# 类绑定方法
def pf(self):
    print('Class Student')

Student.pf = pf

s2 = Student()
s2.pf()

Student.name = 'Student'
print(s2.name)

print('-----------------')

class Std(object):
    __slots__ = ('name', 'age')

t = Std()
t.name = 'xiaoming'
#t.score = 90

class Lihong(Std):
    __slots__ = ('city')
    pass

l = Lihong()
l.name = 'lihong'
l.age = 20
#l.score = 98
l.city = 'GZ'



